# Menaion System Analysis & Implementation Plan

## Executive Summary

The Menaion contains the **"assembly instructions"** (typikon rubrics) that tell us how to combine:
- **Octoechos** texts (tone-based, weekly rotation)
- **Menaion** texts (feast-specific hymnography)
- **Fixed** texts (kathismata, prokeimena, etc.)

This document explains how to implement this database-driven combination system.

---

## What We Have

### 26 Saint Class Templates
All extracted from `/services/menaion/` directory:

| Saint Class | Pages | Size | Rank Mentions |
|-------------|-------|------|---------------|
| Heirarch (Bishop) | 16 | 36KB | Polyeleos, Doxology, Vigil |
| Apostle | 14 | 33KB | Polyeleos, Doxology, Vigil |
| Martyr | 15 | 34KB | Polyeleos, Doxology, Vigil |
| Monastic | 15 | 34KB | Polyeleos, Doxology, Vigil |
| Prophet | 14 | 34KB | Polyeleos, Doxology, Vigil |
| Theotokos | 16 | 36KB | Polyeleos, Doxology, Vigil |
| ... (21 more) | ... | ... | ... |

**Total:** 26 templates covering all saint categories

### Rubrical Structure Identified

Each template contains **conditional assembly rules** based on feast rank:

```
IF feast rank = Polyeleos AND is_sunday:
    Lord I have cried: 10 stichera total
    - 4 from Resurrection (Octoechos)
    - 6 from Saint (Menaion)
    Glory: from the Saint
    Now & Ever: Dogmatic Theotokion (Octoechos, by tone)

IF feast rank = Polyeleos AND NOT is_sunday:
    Lord I have cried: 8 stichera total
    - 0 from Resurrection
    - 8 from Saint (Menaion)
    Glory: from the Saint
    Now & Ever: Theotokion of the Saint

IF feast rank = Doxology (lower):
    Lord I have cried: 6 stichera total
    - 0 from Resurrection (if weekday)
    - 6 from Saint (Menaion)
    Glory: from the Saint
    Now & Ever: Theotokion
```

---

## How the Menaion System Works

### 1. Feast Calendar Structure

Every day of the year (365 days) can have:
- **0+ fixed feasts** (e.g., Sept 8 = Nativity of Theotokos)
- **0+ moveable feasts** (e.g., Pascha, Ascension)
- **Default commemoration** (if no major feast)

### 2. Feast Rank Hierarchy

```
1. GREAT FEAST (Pascha, Nativity, Theophany, etc.)
2. VIGIL (Polyeleos with all-night vigil)
3. POLYELEOS (Blessed is the Man sung, 6 stichera)
4. DOXOLOGY (Great Doxology sung, 6 stichera)
5. SIX STICHERA (6 stichera to the saint)
6. AFTERFEAST (Days following Great Feasts)
7. ORDINARY (Simple commemoration, 3 stichera)
```

**Higher rank takes precedence** when multiple feasts coincide.

### 3. Saint Classification

Each feast is categorized by **saint type** (determines hymnography):
- Apostle / Apostles
- Hierarch / Hierarchs (Bishop/Bishops)
- Martyr / Martyrs / Martyress / Martyresses
- Monastic / Monastics
- Prophet / Prophets
- Hieromartyr / Hieromartyrs (Martyr-Bishops)
- MonasticMartyr / MonasticMartyrs
- Nun / Nuns / NunMartyr
- HieroConfessor
- Fools (Fools for Christ)
- Holy Fathers
- Unmercenaries (Physician-Saints)
- Angels
- Cross (Exaltation of Cross)
- Theotokos (Marian feasts)

**Special:** Some individual saints have unique services (e.g., St. John the Baptist)

---

## Database Implementation

### Enhanced `feasts` Table

```sql
CREATE TABLE feasts (
    feast_id SERIAL PRIMARY KEY,

    -- Identification
    feast_name VARCHAR(255) NOT NULL,
    feast_type VARCHAR(20) NOT NULL CHECK (feast_type IN ('fixed', 'moveable')),

    -- Dating (for FIXED feasts)
    feast_month INT CHECK (feast_month BETWEEN 1 AND 12),
    feast_day INT CHECK (feast_day BETWEEN 1 AND 31),

    -- Dating (for MOVEABLE feasts)
    pascha_offset INT,  -- Days from Pascha

    -- Liturgical classification
    rank INT NOT NULL CHECK (rank BETWEEN 1 AND 7),
    /*
    1 = Great Feast
    2 = Vigil (All-night)
    3 = Polyeleos
    4 = Doxology
    5 = Six Stichera
    6 = Afterfeast
    7 = Ordinary
    */

    -- Saint classification
    saint_class VARCHAR(50),  -- Maps to Menaion template filename
    /*
    'Heirarch', 'Apostle', 'Martyr', 'Monastic', 'Prophet',
    'Theotokos', 'Martyrs', 'Apostles', etc.
    */

    saint_names TEXT[],  -- Array: ['St. Nicholas', 'Bishop of Myra']

    -- Customization
    has_custom_service BOOLEAN DEFAULT FALSE,  -- Does this feast have unique texts?
    service_pdf_filename VARCHAR(255),  -- If custom service exists

    -- Calendar applicability
    applies_to_new_calendar BOOLEAN DEFAULT TRUE,
    applies_to_old_calendar BOOLEAN DEFAULT TRUE,

    -- Additional metadata
    fast_day BOOLEAN DEFAULT FALSE,
    is_temple_feast BOOLEAN DEFAULT FALSE,  -- Can be temple feast

    -- Flexible metadata
    metadata JSONB,
    /*
    Example:
    {
        "troparion_tone": 4,
        "kontakion_tone": 8,
        "commemoration_note": "One of the 12 Great Feasts",
        "typical_readings": ["Hebrews 7:26-8:2", "John 10:9-16"]
    }
    */

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Constraints
    CONSTRAINT feast_date_check CHECK (
        (feast_type = 'fixed' AND feast_month IS NOT NULL AND feast_day IS NOT NULL)
        OR
        (feast_type = 'moveable' AND pascha_offset IS NOT NULL)
    )
);

CREATE INDEX idx_feasts_fixed ON feasts(feast_month, feast_day)
    WHERE feast_type = 'fixed';
CREATE INDEX idx_feasts_moveable ON feasts(pascha_offset)
    WHERE feast_type = 'moveable';
CREATE INDEX idx_feasts_rank ON feasts(rank);
CREATE INDEX idx_feasts_class ON feasts(saint_class);
```

### Sample Feast Data

```sql
-- Great Feast: Nativity of Theotokos
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, rank, saint_class, saint_names, metadata)
VALUES (
    'Nativity of the Most Holy Theotokos',
    'fixed',
    9, 8,  -- September 8
    1,  -- Great Feast
    'Theotokos',
    ARRAY['Most Holy Theotokos'],
    '{"troparion_tone": 4, "is_great_feast": true, "has_forefeast": true, "has_afterfeast": true}'::JSONB
);

-- Polyeleos Rank: St. Nicholas
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, rank, saint_class, saint_names)
VALUES (
    'St. Nicholas the Wonderworker',
    'fixed',
    12, 6,  -- December 6
    3,  -- Polyeleos
    'Heirarch',
    ARRAY['St. Nicholas', 'Archbishop of Myra', 'Wonderworker']
);

-- Doxology Rank: St. John Chrysostom
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, rank, saint_class, saint_names)
VALUES (
    'St. John Chrysostom',
    'fixed',
    11, 13,  -- November 13
    4,  -- Doxology
    'Heirarch',
    ARRAY['St. John Chrysostom', 'Archbishop of Constantinople']
);

-- Moveable Feast: Palm Sunday
INSERT INTO feasts (feast_name, feast_type, pascha_offset, rank, saint_class)
VALUES (
    'Entry of Our Lord into Jerusalem (Palm Sunday)',
    'moveable',
    -7,  -- 7 days before Pascha
    1,  -- Great Feast
    NULL  -- Not a saint feast
);
```

---

## Enhanced `typikon_rules` Table

This table encodes **how to combine** Octoechos + Menaion texts:

```sql
CREATE TABLE typikon_rules (
    rule_id SERIAL PRIMARY KEY,

    -- Rule applicability conditions
    feast_rank INT NOT NULL CHECK (feast_rank BETWEEN 1 AND 7),
    service_type VARCHAR(50) NOT NULL,  -- 'vespers', 'matins', 'liturgy'
    is_sunday BOOLEAN DEFAULT FALSE,
    is_saturday BOOLEAN DEFAULT FALSE,

    -- Special liturgical periods
    during_lent BOOLEAN DEFAULT FALSE,
    during_bright_week BOOLEAN DEFAULT FALSE,
    during_holy_week BOOLEAN DEFAULT FALSE,

    -- Rule description (human-readable)
    rule_description TEXT NOT NULL,

    -- Assembly logic (JSONB structure)
    assembly_logic JSONB NOT NULL,
    /*
    Example for Polyeleos Vespers on Sunday:
    {
        "lord_i_cried": {
            "total_stichera": 10,
            "resurrection_stichera": 4,
            "menaion_stichera": 6,
            "glory": "menaion",
            "now_and_ever": "dogmatic_theotokion",
            "dogmatic_tone_source": "octoechos"
        },
        "theotokion_type": "dogmatic",
        "stavrotheotokion_if": null,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory": "menaion_if_appointed",
            "now_and_ever": "octoechos"
        },
        "prokeimenon": {
            "source": "fixed",
            "weekday_based": true
        },
        "readings": {
            "epistle": "menaion",
            "gospel": "menaion"
        }
    }
    */

    priority INT DEFAULT 100,  -- Lower = higher priority

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(feast_rank, service_type, is_sunday, is_saturday, during_lent, during_bright_week)
);
```

### Sample Typikon Rules

```sql
-- Rule: Polyeleos Vespers on Sunday
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic)
VALUES (
    3,  -- Polyeleos
    'vespers',
    TRUE,
    'Polyeleos feast on Sunday evening: 4 Resurrection + 6 Saint stichera',
    '{
        "lord_i_cried": {
            "total": 10,
            "resurrection": 4,
            "menaion": 6,
            "glory": "menaion",
            "now_and_ever": "dogmatic_theotokion"
        },
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory_menaion_if_appointed": true,
            "now_and_ever": "octoechos_theotokion"
        }
    }'::JSONB
);

-- Rule: Polyeleos Vespers on Weekday
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic)
VALUES (
    3,  -- Polyeleos
    'vespers',
    FALSE,
    'Polyeleos feast on weekday: 8 Saint stichera, no Resurrection texts',
    '{
        "lord_i_cried": {
            "total": 8,
            "resurrection": 0,
            "menaion": 8,
            "glory": "menaion",
            "now_and_ever": "menaion_theotokion"
        },
        "aposticha": {
            "source": "menaion",
            "count": 3,
            "glory": "menaion",
            "now_and_ever": "menaion_theotokion"
        }
    }'::JSONB
);

-- Rule: Doxology Vespers on Sunday
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic)
VALUES (
    4,  -- Doxology
    'vespers',
    TRUE,
    'Doxology feast on Sunday: 4 Resurrection + 6 Saint stichera',
    '{
        "lord_i_cried": {
            "total": 10,
            "resurrection": 4,
            "menaion": 6,
            "glory": "menaion",
            "now_and_ever": "dogmatic_theotokion"
        },
        "aposticha": {
            "source": "octoechos",
            "count": 3
        }
    }'::JSONB
);
```

---

## Implementation Roadmap

### Phase 1: Database Setup (1-2 days)
1. ✅ Deploy PostgreSQL schema (already created)
2. **Populate `feasts` table** with:
   - 12 Great Feasts
   - Major moveable feasts (Palm Sunday, Ascension, etc.)
   - 50+ major saint days (most common)
3. **Populate `typikon_rules` table** with:
   - Polyeleos rules (Sunday/weekday)
   - Doxology rules (Sunday/weekday)
   - Great Feast rules
   - Ordinary commemoration rules

### Phase 2: Menaion Text Extraction (1 week)
1. **Extract all 26 saint class templates**
   - Parse stichera, theotokions, canons
   - Structure as JSON
   - Import to `liturgical_texts` table
   - Tag with `saint_class` field

2. **Create template variables**
   - `{saint_name}` placeholders
   - `{he/she}` gender pronouns
   - Configurable per feast

### Phase 3: Service Generation Engine (1 week)
1. **Build query function:**
   ```sql
   SELECT * FROM generate_vespers(
       p_date := '2024-09-08',
       p_calendar := 'new'
   );
   ```

2. **Implement combining logic:**
   - Look up feast for date
   - Get applicable typikon rule
   - Query Octoechos texts by tone
   - Query Menaion texts by saint_class
   - Merge according to assembly_logic JSONB
   - Return complete service HTML/JSON

3. **Handle edge cases:**
   - Multiple feasts same day (rank precedence)
   - Temple feasts (user-configurable)
   - Lenten modifications
   - Bright Week exceptions

### Phase 4: Complete Feast Calendar (2-3 weeks)
1. **Systematically populate all 365 days:**
   - Research from liturgical calendars
   - Use AI to assist with data entry
   - Cross-reference multiple sources
   - Validate completeness

2. **Handle calendar differences:**
   - New Calendar (Gregorian)
   - Old Calendar (Julian + 13 days)
   - Mark feasts that differ

### Phase 5: Advanced Features (1-2 weeks)
1. **PDF export** of generated services
2. **User customization:**
   - Temple feast configuration
   - Local saint selection
   - Language preferences
3. **API endpoints** for mobile/web apps
4. **Calendar view** interface

---

## Why This Approach Works

### 1. Separates Data from Logic
- **Texts** stored in database (easy to update)
- **Rules** encoded in JSONB (flexible, versioned)
- **Code** just queries and assembles (maintainable)

### 2. Handles Complexity Gracefully
- **Conditional logic** in typikon_rules table
- **Rank precedence** via database queries
- **Multiple feasts** resolved algorithmically

### 3. Extensible
- Add new feasts: INSERT into feasts table
- Add new rules: INSERT into typikon_rules
- Add new texts: INSERT into liturgical_texts
- **No code changes required!**

### 4. Leverages Your Strengths
- **SQL expertise**: Complex queries, JSONB logic
- **Database design**: Normalization, indexing
- **Backend**: Flask API, data modeling

---

## Next Steps: Your Choice

**Option A: Feast Calendar First** *(Recommended)*
1. I help you populate the `feasts` table with major feasts
2. We create typikon rules for top ranks (Polyeleos, Doxology)
3. Extract and import 3-4 saint class templates
4. Build basic service generation function
5. **Demo working Vespers for a major feast!**

**Option B: Complete Menaion Extraction**
1. Extract all 26 saint class templates
2. Parse and structure as JSON
3. Import to database
4. Then build generation engine

**Option C: Build Generation Engine First**
1. Create stored procedure for service assembly
2. Implement typikon rule interpreter
3. Test with sample data
4. Then populate full calendar

---

## Conclusion

The Menaion system is the **"instruction manual"** for combining liturgical texts. By:
1. ✅ Extracting the 26 saint class templates (DONE!)
2. ⏳ Populating the feast calendar
3. ⏳ Encoding typikon rules as JSONB
4. ⏳ Building the assembly engine

We create a **database-driven liturgical generator** that's:
- ✅ Fast (database queries)
- ✅ Accurate (rule-based assembly)
- ✅ Maintainable (data-driven, not code-driven)
- ✅ Extensible (add feasts/rules via SQL)

**What would you like to tackle first?**
