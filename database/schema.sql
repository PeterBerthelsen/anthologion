-- ============================================================
-- ANTHOLOGION DATABASE SCHEMA
-- PostgreSQL Schema for Orthodox Liturgical Text Generator
-- ============================================================

-- ============================================================
-- TABLE 1: FEASTS
-- Stores all fixed and moveable feasts
-- ============================================================
CREATE TABLE feasts (
    feast_id SERIAL PRIMARY KEY,
    feast_name VARCHAR(255) NOT NULL,
    feast_type VARCHAR(20) NOT NULL CHECK (feast_type IN ('fixed', 'moveable')),

    -- For FIXED feasts (e.g., Sept 8 = Nativity of Theotokos)
    feast_month INT CHECK (feast_month BETWEEN 1 AND 12),
    feast_day INT CHECK (feast_day BETWEEN 1 AND 31),

    -- For MOVEABLE feasts (e.g., Palm Sunday = Pascha - 7 days)
    pascha_offset INT,  -- Days from Pascha (negative = before, positive = after)

    -- Liturgical classification
    rank INT NOT NULL CHECK (rank BETWEEN 1 AND 7),
    -- 1=Great Feast, 2=Vigil, 3=Polyeleos, 4=Doxology, 5=Six Verse, 6=Afterfeast, 7=Ordinary

    menaion_type INT CHECK (menaion_type BETWEEN 1 AND 24),
    -- Type of saint (Apostle, Martyr, Hierarch, etc.) - references menaion classes

    saint_names TEXT[],  -- Array of saint names commemorated

    -- Calendar applicability
    applies_to_new_calendar BOOLEAN DEFAULT TRUE,
    applies_to_old_calendar BOOLEAN DEFAULT TRUE,

    -- Additional metadata
    fast_day BOOLEAN DEFAULT FALSE,
    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Constraints
    CONSTRAINT feast_date_check CHECK (
        (feast_type = 'fixed' AND feast_month IS NOT NULL AND feast_day IS NOT NULL)
        OR
        (feast_type = 'moveable' AND pascha_offset IS NOT NULL)
    )
);

CREATE INDEX idx_feasts_fixed_date ON feasts(feast_month, feast_day) WHERE feast_type = 'fixed';
CREATE INDEX idx_feasts_moveable ON feasts(pascha_offset) WHERE feast_type = 'moveable';
CREATE INDEX idx_feasts_rank ON feasts(rank);

-- ============================================================
-- TABLE 2: LITURGICAL TEXTS
-- Stores all hymns, prayers, and variable portions
-- ============================================================
CREATE TABLE liturgical_texts (
    text_id SERIAL PRIMARY KEY,

    -- Source identification
    source VARCHAR(50) NOT NULL CHECK (source IN ('octoechos', 'menaion', 'triodion', 'pentecostarion', 'fixed')),

    -- Service and text type
    service_type VARCHAR(50) NOT NULL CHECK (service_type IN (
        'vespers', 'matins', 'liturgy', 'hours', 'compline', 'nocturns', 'little_vespers'
    )),
    text_type VARCHAR(50) NOT NULL CHECK (text_type IN (
        'sticheron', 'theotokion', 'stavrotheotokion', 'aposticha', 'apolytichion',
        'kontakion', 'kathisma_hymn', 'canon_irmos', 'canon_troparion', 'prokeimenon',
        'alleluia', 'communion_hymn', 'megalynarion'
    )),

    -- For OCTOECHOS texts
    tone INT CHECK (tone BETWEEN 1 AND 8),
    weekday INT CHECK (weekday BETWEEN 0 AND 6),  -- 0=Monday, 6=Sunday

    -- For MENAION texts
    rank INT CHECK (rank BETWEEN 1 AND 7),
    menaion_class VARCHAR(50),  -- 'Martyr', 'Hierarch', 'Apostle', etc.

    -- For TRIODION/PENTECOSTARION texts
    liturgical_period VARCHAR(50),  -- 'lent', 'holy_week', 'bright_week', 'pentecost', etc.
    week_offset INT,  -- Week number (e.g., 3rd week of Lent)

    -- The actual text content
    text_content TEXT NOT NULL,

    -- Ordering and metadata
    text_order INT DEFAULT 1,  -- For ordering multiple stichera, etc.
    verse_text TEXT,  -- Associated psalm verse (for stichera)
    melody_spec TEXT,  -- "Special Melody" instructions
    rubric_notes TEXT,  -- Liturgical instructions

    -- Metadata
    metadata JSONB,  -- Flexible field for additional data

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_texts_octoechos ON liturgical_texts(source, tone, weekday, service_type, text_type)
    WHERE source = 'octoechos';
CREATE INDEX idx_texts_menaion ON liturgical_texts(source, rank, menaion_class, service_type, text_type)
    WHERE source = 'menaion';
CREATE INDEX idx_texts_service ON liturgical_texts(service_type, text_type);

-- ============================================================
-- TABLE 3: TYPIKON RULES
-- Defines how to combine texts from different sources
-- ============================================================
CREATE TABLE typikon_rules (
    rule_id SERIAL PRIMARY KEY,

    -- Conditions for rule applicability
    feast_rank INT NOT NULL CHECK (feast_rank BETWEEN 1 AND 7),
    service_type VARCHAR(50) NOT NULL,
    weekday INT CHECK (weekday BETWEEN 0 AND 6),  -- NULL = applies to all days

    -- Does this day have Menaion/Triodion content?
    has_menaion BOOLEAN DEFAULT FALSE,
    has_triodion BOOLEAN DEFAULT FALSE,
    has_pentecostarion BOOLEAN DEFAULT FALSE,

    -- Rule description
    rule_description TEXT NOT NULL,

    -- Assembly logic (structured JSON)
    assembly_logic JSONB NOT NULL,
    /* Example assembly_logic structure:
    {
        "stichera_lord_i_cried": {
            "total_count": 10,
            "resurrection_stichera": 7,
            "menaion_stichera": 3,
            "note": "Or 4 resurrection and 6 menaion if Polyeleos rank"
        },
        "theotokion": {
            "source": "octoechos",
            "type": "dogmatic",
            "use_stavrotheotokion_if": "wednesday OR friday"
        },
        "aposticha": {
            "source": "octoechos",
            "count": 3
        }
    }
    */

    priority INT DEFAULT 100,  -- Lower number = higher priority

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(feast_rank, service_type, weekday, has_menaion, has_triodion)
);

CREATE INDEX idx_typikon_lookup ON typikon_rules(feast_rank, service_type, weekday);

-- ============================================================
-- TABLE 4: FIXED TEXTS
-- Non-variable prayers, psalms, and structural elements
-- ============================================================
CREATE TABLE fixed_texts (
    fixed_text_id SERIAL PRIMARY KEY,

    text_key VARCHAR(100) UNIQUE NOT NULL,  -- e.g., 'lords_prayer', 'kathisma_1_stasis_1'
    text_category VARCHAR(50) NOT NULL CHECK (text_category IN (
        'prayer', 'kathisma', 'psalm', 'prokeimenon', 'litany', 'dismissal'
    )),

    text_content TEXT NOT NULL,
    text_html TEXT,  -- Pre-formatted HTML version

    -- For kathismata and psalms
    kathisma_number INT CHECK (kathisma_number BETWEEN 1 AND 20),
    stasis_number INT CHECK (stasis_number BETWEEN 1 AND 3),
    psalm_number INT,

    -- For daily prokeimena
    weekday INT CHECK (weekday BETWEEN 0 AND 6),
    tone INT CHECK (tone BETWEEN 1 AND 8),

    metadata JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_fixed_texts_kathisma ON fixed_texts(kathisma_number, stasis_number)
    WHERE text_category = 'kathisma';
CREATE INDEX idx_fixed_texts_prokeimenon ON fixed_texts(text_category, weekday)
    WHERE text_category = 'prokeimenon';

-- ============================================================
-- STORED PROCEDURE: CALCULATE PASCHALION
-- Calculates Pascha date, tone, and liturgical week for a given date
-- ============================================================
CREATE OR REPLACE FUNCTION calculate_paschalion(
    p_year INT,
    p_month INT,
    p_day INT
) RETURNS TABLE (
    pascha_date DATE,
    pentecost_date DATE,
    pascha_offset INT,
    is_pascha BOOLEAN,
    is_pentecost BOOLEAN,
    lent_week INT,
    pascha_week INT,
    weeks_after_pentecost INT,
    weekly_tone INT
) AS $$
DECLARE
    v_date DATE;
    v_pascha DATE;
    v_pentecost DATE;
    v_offset INT;
    v_a INT; v_b INT; v_c INT; v_d INT; v_e INT; v_f INT;
    v_M INT; v_D INT;
    v_tone INT;
    v_lent_week INT;
    v_pascha_week INT;
    v_weeks_after INT;
    v_old_calendar_offset INT := 13;  -- 13 days for 2021-2099
BEGIN
    v_date := make_date(p_year, p_month, p_day);

    -- Calculate Pascha using Julian calendar algorithm
    v_a := p_year % 4;
    v_b := p_year % 7;
    v_c := p_year % 19;
    v_d := ((19 * v_c) + 15) % 30;
    v_e := ((2 * v_a) + (4 * v_b) - v_d + 34) % 7;
    v_f := v_d + v_e + 114;
    v_M := v_f / 31;
    v_D := (v_f % 31) + 1;

    -- Add Old Calendar offset
    v_pascha := make_date(p_year, v_M, v_D) + (v_old_calendar_offset || ' days')::INTERVAL;
    v_pentecost := v_pascha + '49 days'::INTERVAL;
    v_offset := v_date - v_pascha;

    -- Determine liturgical week
    CASE
        WHEN v_offset < -70 THEN
            -- Before Lent - calculate weeks after previous Pentecost
            v_weeks_after := ((v_date - LAG(v_pentecost) OVER (ORDER BY v_date)) - 1) / 7 + 1;
        WHEN v_offset BETWEEN -70 AND -49 THEN
            v_lent_week := (v_offset + 48) / 7;  -- Weeks before Lent (negative)
        WHEN v_offset BETWEEN -48 AND -1 THEN
            v_lent_week := (v_offset + 48) / 7 + 1;  -- Week of Lent
        WHEN v_offset BETWEEN 0 AND 49 THEN
            v_pascha_week := (v_offset / 7) + 1;  -- Week of Pascha
        ELSE
            v_weeks_after := ((v_date - v_pentecost) - 1) / 7 + 1;
    END CASE;

    -- Calculate tone
    IF v_pascha_week IS NOT NULL THEN
        IF v_pascha_week = 1 OR v_pascha_week = 8 THEN
            v_tone := NULL;  -- Bright Week and Pentecost have no tone
        ELSE
            v_tone := v_pascha_week - 1;
        END IF;
    ELSIF v_offset BETWEEN -7 AND -1 THEN
        v_tone := NULL;  -- Holy Week has no tone
    ELSE
        v_tone := (v_offset / 7) % 8;
        v_tone := CASE WHEN v_tone = 0 THEN 8 ELSE v_tone END;
    END IF;

    RETURN QUERY SELECT
        v_pascha,
        v_pentecost,
        v_offset,
        v_date = v_pascha,
        v_date = v_pentecost,
        v_lent_week,
        v_pascha_week,
        v_weeks_after,
        v_tone;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- STORED PROCEDURE: GET SERVICE TEXTS
-- Main procedure to retrieve all texts for a given service
-- ============================================================
CREATE OR REPLACE FUNCTION get_service_texts(
    p_date DATE,
    p_calendar VARCHAR(10),  -- 'new' or 'old'
    p_service_type VARCHAR(50)  -- 'vespers', 'matins', etc.
) RETURNS TABLE (
    section_name VARCHAR(100),
    text_order INT,
    text_content TEXT,
    rubric_notes TEXT,
    metadata JSONB
) AS $$
DECLARE
    v_paschalion RECORD;
    v_feast RECORD;
    v_weekday INT;
    v_tone INT;
    v_rank INT;
    v_rule RECORD;
BEGIN
    -- Calculate paschalion for this date
    SELECT * INTO v_paschalion FROM calculate_paschalion(
        EXTRACT(YEAR FROM p_date)::INT,
        EXTRACT(MONTH FROM p_date)::INT,
        EXTRACT(DAY FROM p_date)::INT
    );

    v_weekday := EXTRACT(DOW FROM p_date)::INT;
    v_tone := v_paschalion.weekly_tone;

    -- Look up feast for this date (if any)
    SELECT * INTO v_feast FROM feasts
    WHERE (
        (feast_type = 'fixed' AND feast_month = EXTRACT(MONTH FROM p_date) AND feast_day = EXTRACT(DAY FROM p_date))
        OR
        (feast_type = 'moveable' AND pascha_offset = v_paschalion.pascha_offset)
    )
    AND (
        (p_calendar = 'new' AND applies_to_new_calendar = TRUE)
        OR
        (p_calendar = 'old' AND applies_to_old_calendar = TRUE)
    )
    ORDER BY rank ASC  -- Highest rank feast takes precedence
    LIMIT 1;

    v_rank := COALESCE(v_feast.rank, 7);  -- Default to ordinary if no feast

    -- Get applicable typikon rule
    SELECT * INTO v_rule FROM typikon_rules
    WHERE feast_rank = v_rank
    AND service_type = p_service_type
    AND (weekday IS NULL OR weekday = v_weekday)
    ORDER BY priority ASC
    LIMIT 1;

    -- TODO: Use v_rule.assembly_logic to construct the service
    -- This would query liturgical_texts based on the JSON rules
    -- For now, return a placeholder

    RETURN QUERY SELECT
        'placeholder'::VARCHAR(100),
        1::INT,
        'Service generation logic to be implemented'::TEXT,
        NULL::TEXT,
        NULL::JSONB;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- SAMPLE DATA INSERTS
-- ============================================================

-- Insert a few sample feasts
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, rank, menaion_type, saint_names, applies_to_new_calendar, applies_to_old_calendar)
VALUES
    ('Nativity of the Theotokos', 'fixed', 9, 8, 2, 2, ARRAY['Most Holy Theotokos'], TRUE, TRUE),
    ('Exaltation of the Cross', 'fixed', 9, 14, 1, 3, ARRAY[], TRUE, TRUE),
    ('Palm Sunday', 'moveable', NULL, NULL, -7, 1, ARRAY[], TRUE, TRUE),
    ('Pascha - Resurrection of Christ', 'moveable', NULL, NULL, 0, 1, ARRAY[], TRUE, TRUE);

-- Insert sample fixed text (Lord's Prayer)
INSERT INTO fixed_texts (text_key, text_category, text_content)
VALUES (
    'lords_prayer',
    'prayer',
    'Our Father, Who art in the heavens, hallowed be Thy name. Thy kingdom come, Thy will be done, on earth as it is in heaven. Give us this day our daily bread, and forgive us our debts, as we forgive our debtors; and lead us not into temptation, but deliver us from the evil one.'
);

-- ============================================================
-- COMMENTS
-- ============================================================
COMMENT ON TABLE feasts IS 'Stores all Orthodox feast days (fixed and moveable)';
COMMENT ON TABLE liturgical_texts IS 'Stores all variable liturgical hymns and prayers';
COMMENT ON TABLE typikon_rules IS 'Defines assembly rules for combining texts based on feast rank';
COMMENT ON TABLE fixed_texts IS 'Stores non-variable prayers, psalms, and kathismata';
COMMENT ON FUNCTION calculate_paschalion IS 'Calculates Paschalion data for any given date';
COMMENT ON FUNCTION get_service_texts IS 'Main function to retrieve complete service texts';
