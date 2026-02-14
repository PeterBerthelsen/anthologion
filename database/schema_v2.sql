-- ============================================================
-- ANTHOLOGION DATABASE SCHEMA v2.0
-- PostgreSQL Schema for Orthodox Liturgical Text Generator
--
-- This replaces the original schema.sql with:
-- 1. Enhanced feasts table (saint_class instead of menaion_type)
-- 2. Updated typikon_rules (is_sunday/is_saturday fields)
-- 3. Complete generate_vespers() stored procedure
-- 4. Improved calculate_paschalion()
-- ============================================================

-- Drop existing objects if they exist (for clean re-deployment)
DROP FUNCTION IF EXISTS generate_vespers(DATE, VARCHAR) CASCADE;
DROP FUNCTION IF EXISTS get_service_texts(DATE, VARCHAR, VARCHAR) CASCADE;
DROP FUNCTION IF EXISTS calculate_paschalion(INT, INT, INT) CASCADE;
DROP FUNCTION IF EXISTS get_feast_for_date(DATE, VARCHAR) CASCADE;
DROP TABLE IF EXISTS typikon_rules CASCADE;
DROP TABLE IF EXISTS liturgical_texts CASCADE;
DROP TABLE IF EXISTS fixed_texts CASCADE;
DROP TABLE IF EXISTS feasts CASCADE;

-- ============================================================
-- TABLE 1: FEASTS
-- ============================================================
CREATE TABLE feasts (
    feast_id SERIAL PRIMARY KEY,
    feast_name VARCHAR(255) NOT NULL,
    feast_type VARCHAR(20) NOT NULL CHECK (feast_type IN ('fixed', 'moveable')),

    -- For FIXED feasts
    feast_month INT CHECK (feast_month BETWEEN 1 AND 12),
    feast_day INT CHECK (feast_day BETWEEN 1 AND 31),

    -- For MOVEABLE feasts (days from Pascha)
    pascha_offset INT,

    -- Liturgical classification
    rank INT NOT NULL CHECK (rank BETWEEN 1 AND 7),
    -- 1=Great Feast, 2=Vigil, 3=Polyeleos, 4=Doxology,
    -- 5=Six Stichera, 6=Afterfeast, 7=Ordinary

    -- Saint classification (maps to Menaion template)
    saint_class VARCHAR(50),
    -- One of: 'Heirarch','Heirarchs','Apostle','Apostles','Martyr','Martyrs',
    -- 'Martyress','Martyresses','Monastic','Monastics','Prophet','Hieromartyr',
    -- 'Heiromartyrs','MonasticMartyr','MonasticMartyrs','HieroConfessor',
    -- 'Nun','NunMartyr','Nuns','Fools','Holy Fathers','Unmercenaries',
    -- 'Angels','Cross','Theotokos','St John Baptist'

    saint_names TEXT[] DEFAULT '{}',
    has_custom_service BOOLEAN DEFAULT FALSE,

    -- Calendar
    applies_to_new_calendar BOOLEAN DEFAULT TRUE,
    applies_to_old_calendar BOOLEAN DEFAULT TRUE,
    fast_day BOOLEAN DEFAULT FALSE,

    -- Flexible metadata (troparion_tone, kontakion_tone, readings, etc.)
    metadata JSONB DEFAULT '{}',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT feast_date_check CHECK (
        (feast_type = 'fixed' AND feast_month IS NOT NULL AND feast_day IS NOT NULL)
        OR
        (feast_type = 'moveable' AND pascha_offset IS NOT NULL)
    )
);

CREATE INDEX idx_feasts_fixed ON feasts(feast_month, feast_day) WHERE feast_type = 'fixed';
CREATE INDEX idx_feasts_moveable ON feasts(pascha_offset) WHERE feast_type = 'moveable';
CREATE INDEX idx_feasts_rank ON feasts(rank);
CREATE INDEX idx_feasts_class ON feasts(saint_class);

-- ============================================================
-- TABLE 2: LITURGICAL TEXTS
-- ============================================================
CREATE TABLE liturgical_texts (
    text_id SERIAL PRIMARY KEY,

    -- Source: which liturgical book
    source VARCHAR(50) NOT NULL CHECK (source IN (
        'octoechos', 'menaion', 'triodion', 'pentecostarion', 'fixed'
    )),

    -- Service and text type
    service_type VARCHAR(50) NOT NULL CHECK (service_type IN (
        'vespers', 'matins', 'liturgy', 'hours', 'compline',
        'nocturns', 'little_vespers'
    )),
    text_type VARCHAR(80) NOT NULL CHECK (text_type IN (
        'sticheron', 'theotokion', 'dogmatic_theotokion',
        'stavrotheotokion', 'aposticha', 'aposticha_theotokion',
        'aposticha_stavrotheotokion', 'apolytichion', 'troparion',
        'kontakion', 'ikos', 'kathisma_hymn', 'exapostilarion',
        'canon_irmos', 'canon_troparion', 'prokeimenon',
        'alleluia', 'communion_hymn', 'megalynarion',
        'idiomelon', 'litia_sticheron'
    )),

    -- For OCTOECHOS texts
    tone INT CHECK (tone BETWEEN 1 AND 8),
    weekday INT CHECK (weekday BETWEEN 0 AND 6),  -- 0=Sunday ... 6=Saturday

    -- For MENAION texts (saint class templates)
    saint_class VARCHAR(50),  -- Maps to saint_class in feasts table

    -- The actual text content
    text_content TEXT NOT NULL,

    -- Ordering and metadata
    text_order INT DEFAULT 1,
    verse_text TEXT,
    melody_spec TEXT,  -- "Special Melody" instructions
    rubric_notes TEXT,

    metadata JSONB DEFAULT '{}',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_texts_octoechos ON liturgical_texts(tone, weekday, service_type, text_type)
    WHERE source = 'octoechos';
CREATE INDEX idx_texts_menaion ON liturgical_texts(saint_class, service_type, text_type)
    WHERE source = 'menaion';
CREATE INDEX idx_texts_service ON liturgical_texts(service_type, text_type);

-- ============================================================
-- TABLE 3: TYPIKON RULES
-- ============================================================
CREATE TABLE typikon_rules (
    rule_id SERIAL PRIMARY KEY,

    feast_rank INT NOT NULL CHECK (feast_rank BETWEEN 1 AND 7),
    service_type VARCHAR(50) NOT NULL,

    -- Day-of-week conditions
    is_sunday BOOLEAN DEFAULT FALSE,
    is_saturday BOOLEAN DEFAULT FALSE,

    -- Liturgical period conditions
    during_lent BOOLEAN DEFAULT FALSE,
    during_bright_week BOOLEAN DEFAULT FALSE,
    during_holy_week BOOLEAN DEFAULT FALSE,

    rule_description TEXT NOT NULL,

    -- Assembly instructions as structured JSON
    assembly_logic JSONB NOT NULL,

    priority INT DEFAULT 100,  -- Lower = higher priority

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_typikon_lookup ON typikon_rules(feast_rank, service_type);

-- ============================================================
-- TABLE 4: FIXED TEXTS
-- ============================================================
CREATE TABLE fixed_texts (
    fixed_text_id SERIAL PRIMARY KEY,

    text_key VARCHAR(100) UNIQUE NOT NULL,
    text_category VARCHAR(50) NOT NULL CHECK (text_category IN (
        'prayer', 'kathisma', 'psalm', 'prokeimenon', 'litany',
        'dismissal', 'exclamation', 'rubric'
    )),

    text_content TEXT NOT NULL,
    text_html TEXT,

    kathisma_number INT CHECK (kathisma_number BETWEEN 1 AND 20),
    stasis_number INT CHECK (stasis_number BETWEEN 1 AND 3),
    psalm_number INT,

    weekday INT CHECK (weekday BETWEEN 0 AND 6),
    tone INT CHECK (tone BETWEEN 1 AND 8),

    metadata JSONB DEFAULT '{}',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_fixed_kathisma ON fixed_texts(kathisma_number, stasis_number)
    WHERE text_category = 'kathisma';
CREATE INDEX idx_fixed_prokeimenon ON fixed_texts(text_category, weekday)
    WHERE text_category = 'prokeimenon';

-- ============================================================
-- FUNCTION: CALCULATE PASCHALION
-- Fixed version using proper PL/pgSQL (no window functions)
-- ============================================================
CREATE OR REPLACE FUNCTION calculate_paschalion(p_year INT, p_month INT, p_day INT)
RETURNS TABLE (
    pascha_date DATE,
    pentecost_date DATE,
    pascha_offset INT,
    is_pascha BOOLEAN,
    is_pentecost BOOLEAN,
    lent_week INT,
    pascha_week INT,
    weeks_after_pentecost INT,
    weekly_tone INT,
    is_lent BOOLEAN,
    is_holy_week BOOLEAN,
    is_bright_week BOOLEAN
) AS $$
DECLARE
    v_date DATE;
    v_pascha DATE;
    v_pentecost DATE;
    v_offset INT;
    v_a INT; v_b INT; v_c INT; v_d INT; v_e INT; v_f INT;
    v_M INT; v_D INT;
    v_tone INT;
    v_lent_week INT := NULL;
    v_pascha_week INT := NULL;
    v_weeks_after INT := NULL;
    v_is_lent BOOLEAN := FALSE;
    v_is_holy_week BOOLEAN := FALSE;
    v_is_bright_week BOOLEAN := FALSE;
    v_old_cal_offset INT := 13;
BEGIN
    v_date := make_date(p_year, p_month, p_day);

    -- Calculate Pascha (Julian algorithm + Gregorian offset)
    v_a := p_year % 4;
    v_b := p_year % 7;
    v_c := p_year % 19;
    v_d := ((19 * v_c) + 15) % 30;
    v_e := ((2 * v_a) + (4 * v_b) - v_d + 34) % 7;
    v_f := v_d + v_e + 114;
    v_M := v_f / 31;
    v_D := (v_f % 31) + 1;

    v_pascha := make_date(p_year, v_M, v_D) + (v_old_cal_offset || ' days')::INTERVAL;
    v_pentecost := v_pascha + '49 days'::INTERVAL;
    v_offset := v_date - v_pascha;

    -- Determine liturgical period
    IF v_offset BETWEEN -48 AND -8 THEN
        v_is_lent := TRUE;
        v_lent_week := (v_offset + 49) / 7;  -- Week 1-6 of Lent
    ELSIF v_offset BETWEEN -7 AND -1 THEN
        v_is_holy_week := TRUE;
    ELSIF v_offset BETWEEN 0 AND 6 THEN
        v_is_bright_week := TRUE;
        v_pascha_week := 1;
    ELSIF v_offset BETWEEN 7 AND 49 THEN
        v_pascha_week := (v_offset / 7) + 1;
    ELSIF v_offset > 49 THEN
        v_weeks_after := (v_offset - 49) / 7 + 1;
    END IF;

    -- Calculate tone (8-week rotation starting from Pascha)
    IF v_is_bright_week THEN
        v_tone := NULL;  -- All 8 tones sung during Bright Week
    ELSIF v_is_holy_week THEN
        v_tone := NULL;  -- Special services
    ELSIF v_offset >= 7 THEN
        -- After Pascha: tone = ((week_from_pascha - 2) % 8) + 1
        v_tone := ((v_offset / 7 - 1) % 8);
        IF v_tone = 0 THEN v_tone := 8; END IF;
    ELSIF v_offset < -48 THEN
        -- Before Lent: need previous year's Pascha to calculate
        -- Simplified: use a lookup based on weeks before next Pascha
        v_tone := (((v_offset + 490) / 7) % 8);
        IF v_tone = 0 THEN v_tone := 8; END IF;
    ELSIF v_is_lent THEN
        -- During Lent: tone continues from pre-Lenten period
        v_tone := (((v_offset + 490) / 7) % 8);
        IF v_tone = 0 THEN v_tone := 8; END IF;
    END IF;

    RETURN QUERY SELECT
        v_pascha,
        v_pentecost,
        v_offset,
        (v_date = v_pascha),
        (v_date = v_pentecost),
        v_lent_week,
        v_pascha_week,
        v_weeks_after,
        v_tone,
        v_is_lent,
        v_is_holy_week,
        v_is_bright_week;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- ============================================================
-- FUNCTION: GET FEAST FOR DATE
-- Looks up the highest-ranked feast for a given date
-- ============================================================
CREATE OR REPLACE FUNCTION get_feast_for_date(
    p_date DATE,
    p_calendar VARCHAR(10) DEFAULT 'new'
)
RETURNS TABLE (
    feast_id INT,
    feast_name VARCHAR(255),
    rank INT,
    saint_class VARCHAR(50),
    saint_names TEXT[],
    has_custom_service BOOLEAN,
    metadata JSONB
) AS $$
DECLARE
    v_month INT;
    v_day INT;
    v_paschalion RECORD;
BEGIN
    v_month := EXTRACT(MONTH FROM p_date);
    v_day := EXTRACT(DAY FROM p_date);

    -- Get paschalion for moveable feast lookup
    SELECT * INTO v_paschalion FROM calculate_paschalion(
        EXTRACT(YEAR FROM p_date)::INT, v_month, v_day
    );

    -- Return highest-ranked feast (fixed or moveable)
    RETURN QUERY
    SELECT f.feast_id, f.feast_name, f.rank, f.saint_class,
           f.saint_names, f.has_custom_service, f.metadata
    FROM feasts f
    WHERE (
        -- Fixed feast matching
        (f.feast_type = 'fixed' AND f.feast_month = v_month AND f.feast_day = v_day)
        OR
        -- Moveable feast matching
        (f.feast_type = 'moveable' AND f.pascha_offset = v_paschalion.pascha_offset)
    )
    AND (
        (p_calendar = 'new' AND f.applies_to_new_calendar = TRUE)
        OR
        (p_calendar = 'old' AND f.applies_to_old_calendar = TRUE)
        OR
        (p_calendar NOT IN ('new', 'old'))
    )
    ORDER BY f.rank ASC  -- Lowest rank number = highest priority
    LIMIT 1;
END;
$$ LANGUAGE plpgsql STABLE;

-- ============================================================
-- FUNCTION: GENERATE VESPERS
-- The main service assembly engine!
--
-- This function:
-- 1. Calculates the paschalion (tone, liturgical period)
-- 2. Looks up the feast for the date
-- 3. Finds the applicable typikon rule
-- 4. Queries Octoechos and Menaion texts
-- 5. Combines them according to the assembly_logic
-- 6. Returns ordered service sections
-- ============================================================
CREATE OR REPLACE FUNCTION generate_vespers(
    p_date DATE,
    p_calendar VARCHAR(10) DEFAULT 'new'
)
RETURNS TABLE (
    section_name TEXT,
    section_order INT,
    text_order INT,
    source TEXT,
    text_type TEXT,
    tone INT,
    text_content TEXT,
    verse_text TEXT,
    rubric TEXT
) AS $$
DECLARE
    v_paschalion RECORD;
    v_feast RECORD;
    v_rule RECORD;
    v_assembly JSONB;
    v_tone INT;
    v_weekday INT;  -- 0=Sunday, 6=Saturday (PostgreSQL DOW)
    v_is_sunday BOOLEAN;
    v_is_saturday BOOLEAN;
    v_saint_class VARCHAR(50);
    v_feast_rank INT;
    v_section_counter INT := 0;

    -- Assembly variables from JSONB
    v_lord_i_cried JSONB;
    v_resurrection_count INT;
    v_menaion_count INT;
    v_octoechos_count INT;
    v_aposticha JSONB;
BEGIN
    -- ======================================
    -- STEP 1: Calculate paschalion
    -- ======================================
    SELECT * INTO v_paschalion FROM calculate_paschalion(
        EXTRACT(YEAR FROM p_date)::INT,
        EXTRACT(MONTH FROM p_date)::INT,
        EXTRACT(DAY FROM p_date)::INT
    );

    v_tone := v_paschalion.weekly_tone;
    v_weekday := EXTRACT(DOW FROM p_date)::INT;  -- 0=Sunday
    v_is_sunday := (v_weekday = 0);
    v_is_saturday := (v_weekday = 6);

    -- ======================================
    -- STEP 2: Look up feast
    -- ======================================
    SELECT * INTO v_feast FROM get_feast_for_date(p_date, p_calendar);

    v_feast_rank := COALESCE(v_feast.rank, 7);
    v_saint_class := v_feast.saint_class;

    -- ======================================
    -- STEP 3: Find typikon rule
    -- ======================================
    SELECT * INTO v_rule FROM typikon_rules tr
    WHERE tr.feast_rank = v_feast_rank
    AND tr.service_type = 'vespers'
    AND tr.is_sunday = v_is_sunday
    AND (tr.during_lent = v_paschalion.is_lent OR tr.during_lent = FALSE)
    ORDER BY tr.priority ASC
    LIMIT 1;

    -- If no specific rule, try a generic one
    IF v_rule IS NULL THEN
        SELECT * INTO v_rule FROM typikon_rules tr
        WHERE tr.feast_rank = v_feast_rank
        AND tr.service_type = 'vespers'
        AND tr.is_sunday = FALSE
        ORDER BY tr.priority ASC
        LIMIT 1;
    END IF;

    -- If still no rule, use a default
    IF v_rule IS NULL THEN
        -- Return header info only
        v_section_counter := v_section_counter + 1;
        RETURN QUERY SELECT
            'header'::TEXT,
            v_section_counter,
            1,
            'system'::TEXT,
            'rubric'::TEXT,
            v_tone,
            format('Vespers for %s — Tone %s — %s',
                p_date::TEXT,
                COALESCE(v_tone::TEXT, 'N/A'),
                COALESCE(v_feast.feast_name, 'Ordinary Day')
            ),
            NULL::TEXT,
            'No typikon rule found for this rank/day combination'::TEXT;
        RETURN;
    END IF;

    v_assembly := v_rule.assembly_logic;

    -- ======================================
    -- STEP 4: Generate service header
    -- ======================================
    v_section_counter := v_section_counter + 1;
    RETURN QUERY SELECT
        'header'::TEXT,
        v_section_counter,
        1,
        'system'::TEXT,
        'rubric'::TEXT,
        v_tone,
        format('VESPERS — %s — Tone %s',
            COALESCE(v_feast.feast_name, 'Ordinary Day'),
            COALESCE(v_tone::TEXT, 'N/A')
        ),
        NULL::TEXT,
        format('Rank: %s | Rule: %s',
            CASE v_feast_rank
                WHEN 1 THEN 'Great Feast'
                WHEN 2 THEN 'Vigil'
                WHEN 3 THEN 'Polyeleos'
                WHEN 4 THEN 'Doxology'
                WHEN 5 THEN 'Six Stichera'
                WHEN 6 THEN 'Afterfeast'
                WHEN 7 THEN 'Ordinary'
            END,
            v_rule.rule_description
        )::TEXT;

    -- ======================================
    -- STEP 5: Lord I have cried — Stichera
    -- ======================================
    v_lord_i_cried := v_assembly -> 'lord_i_cried';

    IF v_lord_i_cried IS NOT NULL THEN
        v_section_counter := v_section_counter + 1;

        -- Section rubric
        RETURN QUERY SELECT
            'lord_i_cried'::TEXT,
            v_section_counter,
            0,
            'rubric'::TEXT,
            'rubric'::TEXT,
            NULL::INT,
            format('On "Lord, I have cried...", %s Stichera:',
                (v_lord_i_cried ->> 'total')::TEXT
            ),
            NULL::TEXT,
            v_rule.rule_description::TEXT;

        -- Resurrection stichera (from Octoechos)
        v_resurrection_count := COALESCE((v_lord_i_cried ->> 'resurrection')::INT, 0);
        IF v_resurrection_count > 0 AND v_tone IS NOT NULL THEN
            RETURN QUERY
            SELECT
                'lord_i_cried'::TEXT,
                v_section_counter,
                lt.text_order,
                'octoechos'::TEXT,
                lt.text_type::TEXT,
                lt.tone,
                lt.text_content,
                lt.verse_text,
                'Resurrection Stichera'::TEXT
            FROM liturgical_texts lt
            WHERE lt.source = 'octoechos'
            AND lt.service_type = 'vespers'
            AND lt.text_type = 'sticheron'
            AND lt.tone = v_tone
            AND lt.weekday = v_weekday
            ORDER BY lt.text_order
            LIMIT v_resurrection_count;
        END IF;

        -- Octoechos stichera (non-resurrection, for weekdays)
        v_octoechos_count := COALESCE((v_lord_i_cried ->> 'octoechos')::INT, 0);
        IF v_octoechos_count > 0 AND v_tone IS NOT NULL THEN
            RETURN QUERY
            SELECT
                'lord_i_cried'::TEXT,
                v_section_counter,
                lt.text_order + 100,  -- Offset to order after resurrection
                'octoechos'::TEXT,
                lt.text_type::TEXT,
                lt.tone,
                lt.text_content,
                lt.verse_text,
                'Octoechos Stichera'::TEXT
            FROM liturgical_texts lt
            WHERE lt.source = 'octoechos'
            AND lt.service_type = 'vespers'
            AND lt.text_type = 'sticheron'
            AND lt.tone = v_tone
            AND lt.weekday = v_weekday
            ORDER BY lt.text_order
            LIMIT v_octoechos_count;
        END IF;

        -- Menaion stichera (from saint template)
        v_menaion_count := COALESCE((v_lord_i_cried ->> 'menaion')::INT, 0);
        IF v_menaion_count > 0 AND v_saint_class IS NOT NULL THEN
            RETURN QUERY
            SELECT
                'lord_i_cried'::TEXT,
                v_section_counter,
                lt.text_order + 200,  -- Offset to order after octoechos
                'menaion'::TEXT,
                lt.text_type::TEXT,
                lt.tone,
                -- Replace {saint_name} placeholder with actual saint name
                REPLACE(lt.text_content, '{saint_name}',
                    COALESCE(v_feast.saint_names[1], 'N/N')),
                lt.verse_text,
                format('Stichera of the Saint (%s)', v_saint_class)::TEXT
            FROM liturgical_texts lt
            WHERE lt.source = 'menaion'
            AND lt.service_type = 'vespers'
            AND lt.text_type = 'sticheron'
            AND lt.saint_class = v_saint_class
            ORDER BY lt.text_order
            LIMIT v_menaion_count;
        END IF;

        -- Glory / Theotokion
        v_section_counter := v_section_counter + 1;

        -- Determine Glory source
        IF (v_lord_i_cried ->> 'glory') = 'menaion' AND v_saint_class IS NOT NULL THEN
            -- Glory from Menaion (saint's idiomelon)
            RETURN QUERY
            SELECT
                'glory'::TEXT,
                v_section_counter,
                1,
                'menaion'::TEXT,
                'idiomelon'::TEXT,
                lt.tone,
                REPLACE(lt.text_content, '{saint_name}',
                    COALESCE(v_feast.saint_names[1], 'N/N')),
                NULL::TEXT,
                'Glory...'::TEXT
            FROM liturgical_texts lt
            WHERE lt.source = 'menaion'
            AND lt.service_type = 'vespers'
            AND lt.text_type = 'idiomelon'
            AND lt.saint_class = v_saint_class
            ORDER BY lt.text_order
            LIMIT 1;
        END IF;

        -- Determine Now & Ever source
        IF (v_lord_i_cried ->> 'now_and_ever') = 'dogmatic_theotokion' AND v_tone IS NOT NULL THEN
            -- Dogmatic Theotokion from Octoechos (by tone)
            RETURN QUERY
            SELECT
                'now_and_ever'::TEXT,
                v_section_counter,
                2,
                'octoechos'::TEXT,
                'dogmatic_theotokion'::TEXT,
                lt.tone,
                lt.text_content,
                NULL::TEXT,
                'Now & Ever... Dogmatic Theotokion'::TEXT
            FROM liturgical_texts lt
            WHERE lt.source = 'octoechos'
            AND lt.service_type = 'vespers'
            AND lt.text_type = 'dogmatic_theotokion'
            AND lt.tone = v_tone
            ORDER BY lt.text_order
            LIMIT 1;
        ELSIF (v_lord_i_cried ->> 'now_and_ever') IN ('menaion_theotokion', 'feast') AND v_saint_class IS NOT NULL THEN
            -- Theotokion from Menaion
            RETURN QUERY
            SELECT
                'now_and_ever'::TEXT,
                v_section_counter,
                2,
                'menaion'::TEXT,
                'theotokion'::TEXT,
                lt.tone,
                lt.text_content,
                NULL::TEXT,
                'Now & Ever... Theotokion'::TEXT
            FROM liturgical_texts lt
            WHERE lt.source = 'menaion'
            AND lt.service_type = 'vespers'
            AND lt.text_type = 'theotokion'
            AND lt.saint_class = v_saint_class
            ORDER BY lt.text_order
            LIMIT 1;
        END IF;
    END IF;

    -- ======================================
    -- STEP 6: Prokeimenon
    -- ======================================
    v_section_counter := v_section_counter + 1;
    RETURN QUERY
    SELECT
        'prokeimenon'::TEXT,
        v_section_counter,
        1,
        'fixed'::TEXT,
        'prokeimenon'::TEXT,
        ft.tone,
        ft.text_content,
        NULL::TEXT,
        'Prokeimenon of the Day'::TEXT
    FROM fixed_texts ft
    WHERE ft.text_category = 'prokeimenon'
    AND ft.weekday = v_weekday
    LIMIT 1;

    -- ======================================
    -- STEP 7: Aposticha
    -- ======================================
    v_aposticha := v_assembly -> 'aposticha';

    IF v_aposticha IS NOT NULL THEN
        v_section_counter := v_section_counter + 1;

        RETURN QUERY SELECT
            'aposticha'::TEXT,
            v_section_counter,
            0,
            'rubric'::TEXT,
            'rubric'::TEXT,
            NULL::INT,
            'On the Aposticha:'::TEXT,
            NULL::TEXT,
            NULL::TEXT;

        IF (v_aposticha ->> 'source') = 'octoechos' AND v_tone IS NOT NULL THEN
            -- Aposticha from Octoechos
            RETURN QUERY
            SELECT
                'aposticha'::TEXT,
                v_section_counter,
                lt.text_order,
                'octoechos'::TEXT,
                lt.text_type::TEXT,
                lt.tone,
                lt.text_content,
                lt.verse_text,
                'Aposticha Stichera'::TEXT
            FROM liturgical_texts lt
            WHERE lt.source = 'octoechos'
            AND lt.service_type = 'vespers'
            AND lt.text_type = 'aposticha'
            AND lt.tone = v_tone
            AND lt.weekday = v_weekday
            ORDER BY lt.text_order
            LIMIT COALESCE((v_aposticha ->> 'count')::INT, 3);
        ELSIF (v_aposticha ->> 'source') = 'menaion' AND v_saint_class IS NOT NULL THEN
            -- Aposticha from Menaion
            RETURN QUERY
            SELECT
                'aposticha'::TEXT,
                v_section_counter,
                lt.text_order,
                'menaion'::TEXT,
                lt.text_type::TEXT,
                lt.tone,
                REPLACE(lt.text_content, '{saint_name}',
                    COALESCE(v_feast.saint_names[1], 'N/N')),
                lt.verse_text,
                'Aposticha of the Saint'::TEXT
            FROM liturgical_texts lt
            WHERE lt.source = 'menaion'
            AND lt.service_type = 'vespers'
            AND lt.text_type = 'aposticha'
            AND lt.saint_class = v_saint_class
            ORDER BY lt.text_order
            LIMIT COALESCE((v_aposticha ->> 'count')::INT, 3);
        END IF;

        -- Aposticha Glory from Menaion (if appointed)
        IF (v_aposticha ->> 'glory') IN ('menaion', 'menaion_if_appointed')
           AND v_saint_class IS NOT NULL THEN
            RETURN QUERY
            SELECT
                'aposticha_glory'::TEXT,
                v_section_counter,
                100,
                'menaion'::TEXT,
                'aposticha_theotokion'::TEXT,
                lt.tone,
                REPLACE(lt.text_content, '{saint_name}',
                    COALESCE(v_feast.saint_names[1], 'N/N')),
                NULL::TEXT,
                'Glory... Now & Ever...'::TEXT
            FROM liturgical_texts lt
            WHERE lt.source = 'menaion'
            AND lt.service_type = 'vespers'
            AND lt.text_type = 'aposticha_theotokion'
            AND lt.saint_class = v_saint_class
            ORDER BY lt.text_order
            LIMIT 1;
        END IF;
    END IF;

    -- ======================================
    -- STEP 8: Troparion / Apolytichion
    -- ======================================
    v_section_counter := v_section_counter + 1;

    -- Resurrection troparion (on Sundays)
    IF v_is_sunday AND v_tone IS NOT NULL THEN
        RETURN QUERY
        SELECT
            'troparion'::TEXT,
            v_section_counter,
            1,
            'octoechos'::TEXT,
            'troparion'::TEXT,
            lt.tone,
            lt.text_content,
            NULL::TEXT,
            'Resurrection Troparion'::TEXT
        FROM liturgical_texts lt
        WHERE lt.source = 'octoechos'
        AND lt.service_type = 'vespers'
        AND lt.text_type = 'troparion'
        AND lt.tone = v_tone
        ORDER BY lt.text_order
        LIMIT 1;
    END IF;

    -- Saint's troparion (if feast)
    IF v_saint_class IS NOT NULL THEN
        RETURN QUERY
        SELECT
            'troparion'::TEXT,
            v_section_counter,
            2,
            'menaion'::TEXT,
            'troparion'::TEXT,
            lt.tone,
            REPLACE(lt.text_content, '{saint_name}',
                COALESCE(v_feast.saint_names[1], 'N/N')),
            NULL::TEXT,
            format('Troparion of %s', COALESCE(v_feast.saint_names[1], 'the Saint'))::TEXT
        FROM liturgical_texts lt
        WHERE lt.source = 'menaion'
        AND lt.service_type = 'vespers'
        AND lt.text_type = 'troparion'
        AND lt.saint_class = v_saint_class
        ORDER BY lt.text_order
        LIMIT 1;
    END IF;

    -- ======================================
    -- STEP 9: Dismissal
    -- ======================================
    v_section_counter := v_section_counter + 1;
    RETURN QUERY SELECT
        'dismissal'::TEXT,
        v_section_counter,
        1,
        'fixed'::TEXT,
        'dismissal'::TEXT,
        NULL::INT,
        'And the Dismissal.'::TEXT,
        NULL::TEXT,
        NULL::TEXT;

END;
$$ LANGUAGE plpgsql STABLE;

-- ============================================================
-- COMMENTS
-- ============================================================
COMMENT ON TABLE feasts IS 'All Orthodox feast days (fixed and moveable) with rank and saint classification';
COMMENT ON TABLE liturgical_texts IS 'All variable liturgical hymns indexed by source, tone, weekday, and saint class';
COMMENT ON TABLE typikon_rules IS 'Assembly rules defining how to combine Octoechos + Menaion by feast rank';
COMMENT ON TABLE fixed_texts IS 'Non-variable texts: kathismata, prokeimena, prayers, psalms';
COMMENT ON FUNCTION calculate_paschalion IS 'Calculates Pascha date, tone, and liturgical period for any date';
COMMENT ON FUNCTION get_feast_for_date IS 'Looks up the highest-ranked feast for a given date';
COMMENT ON FUNCTION generate_vespers IS 'Main service assembly engine: generates complete Vespers by date';
