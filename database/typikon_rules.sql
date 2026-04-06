-- =============================================================================
-- TYPIKON RULES: Octoechos + Menaion Assembly Logic
-- =============================================================================
--
-- This file encodes the rubrical rules (typikon) for combining hymns from the
-- Octoechos (the eight-tone cycle) and Menaion (fixed calendar) for each
-- service, depending on feast rank and day of week.
--
-- FEAST RANKS:
--   1 = Great Feast (Theotokos feasts, Transfiguration, Exaltation, etc.)
--   2 = Vigil-rank saint (all-night vigil is served)
--   3 = Polyeleos-rank saint (Ps 134-135 sung at matins)
--   4 = Doxology-rank saint (Great Doxology sung at matins)
--   5 = Six-stichera saint (6 stichera at Lord I Have Cried)
--   6 = Common saint (not used in this file; falls under rank 7 logic)
--   7 = Ordinary / no feast (daily Octoechos cycle predominates)
--
-- ASSEMBLY_LOGIC JSON FIELDS (Vespers):
--   lord_i_cried.total          - Total stichera sung at "Lord I Have Cried"
--   lord_i_cried.resurrection   - How many are resurrection stichera (Octoechos)
--   lord_i_cried.octoechos      - How many are from weekday Octoechos (non-Sunday)
--   lord_i_cried.menaion        - How many are from the Menaion (saint/feast)
--   lord_i_cried.glory          - Source for the "Glory" sticheron
--   lord_i_cried.now_and_ever   - Source for the "Now and ever" sticheron
--   entrance                    - Whether the Little Entrance occurs at vespers
--   readings_count              - Number of Old Testament readings (paroemiae)
--   aposticha.source            - Primary source for aposticha stichera
--   aposticha.count             - Number of aposticha stichera
--   aposticha.glory             - Source for aposticha Glory
--   aposticha.now_and_ever      - Source for aposticha Now-and-ever
--   aposticha.glory_now_and_ever - Combined Glory/Now-and-ever when same source
--   litia                       - Whether litia (procession with blessing) occurs
--   troparion                   - Single troparion source
--   troparion_order             - Ordered list of troparia at end of vespers
--
-- ASSEMBLY_LOGIC JSON FIELDS (Matins):
--   god_is_the_lord.troparion_order - Troparia after "God is the Lord"
--   kathisma_hymns.source           - Source of sedalen hymns after kathismata
--   polyeleos                       - Whether Pss 134-135 are sung
--   magnification                   - Whether a magnification verse is sung
--   canon.resurrection_canon        - Include resurrection canon from Octoechos
--   canon.theotokos_canon           - Include Theotokos canon from Octoechos
--   canon.menaion_canon             - Include canon from Menaion
--   canon.total_troparia_per_ode    - Target troparia count per ode (with irmos)
--   after_canon.exapostilarion       - Source/order of exapostilaria
--   after_canon.praises_stichera     - Stichera at the Praises (Lauds)
--   great_doxology                   - Whether the Great Doxology is sung (vs read)
--
-- CONFLICT RESOLUTION:
--   When multiple rules match a given day, the rule with the LOWEST priority
--   number takes precedence (priority 1 overrides priority 100). Within the
--   same priority, the more specific rule wins: check is_sunday/is_saturday,
--   then during_lent / during_bright_week / during_holy_week flags.
--
-- SPECIAL CASES:
--   - Saturday evening vespers is liturgically Sunday; use is_sunday=TRUE rules
--     because vespers begins the new liturgical day at sunset.
--   - During Bright Week (Pascha through Thomas Sunday), the Pentecostarion
--     replaces both Octoechos and Menaion entirely; these rules do not apply.
--   - During Holy Week, all regular Menaion/Octoechos combinations are
--     suspended; dedicated Triodion services are used instead.
--   - During Great Lent weekdays, certain modifications apply (no Little
--     Entrance at vespers, Lenten aposticha replace Octoechos, etc.).
-- =============================================================================

-- Ensure the table exists
CREATE TABLE IF NOT EXISTS typikon_rules (
    rule_id SERIAL PRIMARY KEY,
    feast_rank INT NOT NULL CHECK (feast_rank BETWEEN 1 AND 7),
    service_type VARCHAR(50) NOT NULL,
    is_sunday BOOLEAN DEFAULT FALSE,
    is_saturday BOOLEAN DEFAULT FALSE,
    during_lent BOOLEAN DEFAULT FALSE,
    during_bright_week BOOLEAN DEFAULT FALSE,
    during_holy_week BOOLEAN DEFAULT FALSE,
    rule_description TEXT NOT NULL,
    assembly_logic JSONB NOT NULL,
    priority INT DEFAULT 100,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(feast_rank, service_type, is_sunday, is_saturday, during_lent, during_bright_week)
);

-- Clear any existing rules to make this script idempotent
DELETE FROM typikon_rules;

-- =============================================================================
-- VESPERS RULES
-- =============================================================================

-- ---------------------------------------------------------------------------
-- RANK 1: Great Feast - Vespers
-- ---------------------------------------------------------------------------

-- Rule 1: Great Feast on Sunday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (1, 'vespers', TRUE,
    'Great Feast on Sunday: the entire service is from the feast; Octoechos resurrection stichera are omitted.',
    '{
        "lord_i_cried": {
            "total": 8,
            "resurrection": 0,
            "menaion": 8,
            "glory": "feast",
            "now_and_ever": "feast"
        },
        "entrance": true,
        "readings_count": 3,
        "aposticha": {
            "source": "feast",
            "count": 3,
            "glory": "feast",
            "now_and_ever": "feast"
        },
        "litia": true,
        "troparion": "feast"
    }'::jsonb, 10);

-- Rule 2: Great Feast on Weekday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (1, 'vespers', FALSE,
    'Great Feast on weekday: the entire service is from the feast; no Octoechos material is used.',
    '{
        "lord_i_cried": {
            "total": 8,
            "resurrection": 0,
            "menaion": 8,
            "glory": "feast",
            "now_and_ever": "feast"
        },
        "entrance": true,
        "readings_count": 3,
        "aposticha": {
            "source": "feast",
            "count": 3,
            "glory": "feast",
            "now_and_ever": "feast"
        },
        "litia": true,
        "troparion": "feast"
    }'::jsonb, 10);

-- ---------------------------------------------------------------------------
-- RANK 2: Vigil-rank Saint - Vespers
-- ---------------------------------------------------------------------------

-- Rule 3: Vigil-rank on Sunday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (2, 'vespers', TRUE,
    'Vigil-rank saint on Sunday: 4 resurrection stichera from Octoechos + 6 from Menaion at Lord I Have Cried. Entrance and 3 readings. Litia is served.',
    '{
        "lord_i_cried": {
            "total": 10,
            "resurrection": 4,
            "menaion": 6,
            "glory": "menaion",
            "now_and_ever": "dogmatic_theotokion"
        },
        "entrance": true,
        "readings_count": 3,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory": "menaion",
            "now_and_ever": "octoechos_theotokion"
        },
        "litia": true,
        "troparion_order": ["resurrection", "saint"]
    }'::jsonb, 20);

-- Rule 4: Vigil-rank on Weekday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (2, 'vespers', FALSE,
    'Vigil-rank saint on weekday: 8 stichera from the Menaion at Lord I Have Cried. Entrance and 3 readings. Litia is served.',
    '{
        "lord_i_cried": {
            "total": 8,
            "resurrection": 0,
            "menaion": 8,
            "glory": "menaion",
            "now_and_ever": "menaion_theotokion"
        },
        "entrance": true,
        "readings_count": 3,
        "aposticha": {
            "source": "menaion",
            "count": 3,
            "glory": "menaion",
            "now_and_ever": "menaion_theotokion"
        },
        "litia": true,
        "troparion": "saint"
    }'::jsonb, 20);

-- ---------------------------------------------------------------------------
-- RANK 3: Polyeleos-rank Saint - Vespers
-- ---------------------------------------------------------------------------

-- Rule 5: Polyeleos-rank on Sunday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (3, 'vespers', TRUE,
    'Polyeleos-rank saint on Sunday: 4 resurrection + 6 Menaion stichera. No entrance at vespers (polyeleos distinction is at matins). Aposticha from Octoechos with Menaion Glory if appointed.',
    '{
        "lord_i_cried": {
            "total": 10,
            "resurrection": 4,
            "menaion": 6,
            "glory": "menaion",
            "now_and_ever": "dogmatic_theotokion"
        },
        "entrance": false,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory": "menaion_if_appointed",
            "now_and_ever": "octoechos_theotokion"
        },
        "troparion_order": ["resurrection", "saint"]
    }'::jsonb, 30);

-- Rule 6: Polyeleos-rank on Weekday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (3, 'vespers', FALSE,
    'Polyeleos-rank saint on weekday: 8 Menaion stichera. Entrance with 3 readings. Aposticha from Menaion.',
    '{
        "lord_i_cried": {
            "total": 8,
            "resurrection": 0,
            "menaion": 8,
            "glory": "menaion",
            "now_and_ever": "menaion_theotokion"
        },
        "entrance": true,
        "readings_count": 3,
        "aposticha": {
            "source": "menaion",
            "count": 3,
            "glory": "menaion",
            "now_and_ever": "menaion_theotokion"
        },
        "troparion": "saint"
    }'::jsonb, 30);

-- ---------------------------------------------------------------------------
-- RANK 4: Doxology-rank Saint - Vespers
-- ---------------------------------------------------------------------------

-- Rule 7: Doxology-rank on Sunday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (4, 'vespers', TRUE,
    'Doxology-rank saint on Sunday: 4 resurrection + 6 Menaion stichera. No entrance. Aposticha from Octoechos.',
    '{
        "lord_i_cried": {
            "total": 10,
            "resurrection": 4,
            "menaion": 6,
            "glory": "menaion",
            "now_and_ever": "dogmatic_theotokion"
        },
        "entrance": false,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory": "menaion_if_appointed",
            "now_and_ever": "octoechos_theotokion"
        },
        "troparion_order": ["resurrection", "saint"]
    }'::jsonb, 40);

-- Rule 8: Doxology-rank on Weekday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (4, 'vespers', FALSE,
    'Doxology-rank saint on weekday: 6 Menaion stichera. No entrance. Aposticha from Octoechos with Menaion Glory if appointed.',
    '{
        "lord_i_cried": {
            "total": 6,
            "resurrection": 0,
            "menaion": 6,
            "glory": "menaion",
            "now_and_ever": "menaion_theotokion"
        },
        "entrance": false,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory": "menaion_if_appointed",
            "now_and_ever": "octoechos_theotokion"
        },
        "troparion_order": ["saint", "theotokos"]
    }'::jsonb, 40);

-- ---------------------------------------------------------------------------
-- RANK 5: Six-stichera Saint - Vespers
-- ---------------------------------------------------------------------------

-- Rule 9: Six-stichera on Sunday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (5, 'vespers', TRUE,
    'Six-stichera saint on Sunday: 4 resurrection + 6 Menaion stichera. No entrance. Standard Sunday aposticha from Octoechos.',
    '{
        "lord_i_cried": {
            "total": 10,
            "resurrection": 4,
            "menaion": 6,
            "glory": "menaion",
            "now_and_ever": "dogmatic_theotokion"
        },
        "entrance": false,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory": "menaion_if_appointed",
            "now_and_ever": "octoechos_theotokion"
        },
        "troparion_order": ["resurrection", "saint"]
    }'::jsonb, 50);

-- Rule 10: Six-stichera on Weekday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (5, 'vespers', FALSE,
    'Six-stichera saint on weekday: 3 Octoechos + 3 Menaion stichera. No entrance. Aposticha from Octoechos.',
    '{
        "lord_i_cried": {
            "total": 6,
            "resurrection": 0,
            "octoechos": 3,
            "menaion": 3,
            "glory": "menaion",
            "now_and_ever": "octoechos_theotokion"
        },
        "entrance": false,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory_now_and_ever": "octoechos_theotokion"
        },
        "troparion_order": ["saint", "theotokos"]
    }'::jsonb, 50);

-- ---------------------------------------------------------------------------
-- RANK 7: Ordinary Day - Vespers
-- ---------------------------------------------------------------------------

-- Rule 11: Ordinary Sunday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (7, 'vespers', TRUE,
    'Ordinary Sunday: 7 resurrection stichera + 3 Menaion. Menaion Glory only if specifically appointed; otherwise all from Octoechos.',
    '{
        "lord_i_cried": {
            "total": 10,
            "resurrection": 7,
            "menaion": 3,
            "glory": "menaion_if_appointed",
            "now_and_ever": "dogmatic_theotokion"
        },
        "entrance": false,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory_now_and_ever": "octoechos_theotokion"
        },
        "troparion_order": ["resurrection"]
    }'::jsonb, 70);

-- Rule 12: Ordinary Weekday - Vespers
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (7, 'vespers', FALSE,
    'Ordinary weekday: 3 Octoechos + 3 Menaion stichera. No entrance. Aposticha entirely from Octoechos.',
    '{
        "lord_i_cried": {
            "total": 6,
            "resurrection": 0,
            "octoechos": 3,
            "menaion": 3,
            "glory_now_and_ever": "octoechos_theotokion"
        },
        "entrance": false,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory_now_and_ever": "octoechos_theotokion"
        },
        "troparion_order": ["saint", "theotokos"]
    }'::jsonb, 70);

-- =============================================================================
-- MATINS RULES
-- =============================================================================

-- ---------------------------------------------------------------------------
-- RANK 1: Great Feast - Matins
-- ---------------------------------------------------------------------------

-- Rule 13: Great Feast on Sunday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (1, 'matins', TRUE,
    'Great Feast on Sunday matins: entirely from the feast. Polyeleos and magnification are sung. Great Doxology. Canon entirely from the feast.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["feast"]
        },
        "kathisma_hymns": {
            "source": "feast"
        },
        "polyeleos": true,
        "magnification": true,
        "canon": {
            "resurrection_canon": false,
            "theotokos_canon": false,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "feast",
            "praises_stichera": {
                "total": 8,
                "resurrection": 0,
                "menaion": 8
            }
        },
        "great_doxology": true
    }'::jsonb, 10);

-- Rule 14: Great Feast on Weekday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (1, 'matins', FALSE,
    'Great Feast on weekday matins: entirely from the feast. Polyeleos and magnification. Great Doxology sung.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["feast"]
        },
        "kathisma_hymns": {
            "source": "feast"
        },
        "polyeleos": true,
        "magnification": true,
        "canon": {
            "resurrection_canon": false,
            "theotokos_canon": false,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "feast",
            "praises_stichera": {
                "total": 8,
                "resurrection": 0,
                "menaion": 8
            }
        },
        "great_doxology": true
    }'::jsonb, 10);

-- ---------------------------------------------------------------------------
-- RANK 2: Vigil-rank Saint - Matins
-- ---------------------------------------------------------------------------

-- Rule 15: Vigil-rank on Sunday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (2, 'matins', TRUE,
    'Vigil-rank saint on Sunday matins: resurrection troparia, then saint. Polyeleos sung. Canon: resurrection + Theotokos + Menaion. 4 resurrection + 4 Menaion praises. Great Doxology.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["resurrection", "saint"]
        },
        "kathisma_hymns": {
            "source": "octoechos_and_menaion"
        },
        "polyeleos": true,
        "magnification": false,
        "canon": {
            "resurrection_canon": true,
            "theotokos_canon": true,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "resurrection_then_menaion",
            "praises_stichera": {
                "total": 8,
                "resurrection": 4,
                "menaion": 4
            }
        },
        "great_doxology": true
    }'::jsonb, 20);

-- Rule 16: Vigil-rank on Weekday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (2, 'matins', FALSE,
    'Vigil-rank saint on weekday matins: saint troparion. Polyeleos sung. Canon from Menaion. 8 Menaion praises. Great Doxology.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["saint", "saint"]
        },
        "kathisma_hymns": {
            "source": "menaion"
        },
        "polyeleos": true,
        "magnification": false,
        "canon": {
            "resurrection_canon": false,
            "theotokos_canon": false,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "menaion",
            "praises_stichera": {
                "total": 8,
                "resurrection": 0,
                "menaion": 8
            }
        },
        "great_doxology": true
    }'::jsonb, 20);

-- ---------------------------------------------------------------------------
-- RANK 3: Polyeleos-rank Saint - Matins
-- ---------------------------------------------------------------------------

-- Rule 17: Polyeleos-rank on Sunday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (3, 'matins', TRUE,
    'Polyeleos-rank saint on Sunday matins: resurrection and saint troparia. Polyeleos sung. Full Sunday canon structure with Menaion canon. Great Doxology.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["resurrection", "saint"]
        },
        "kathisma_hymns": {
            "source": "octoechos_and_menaion"
        },
        "polyeleos": true,
        "magnification": false,
        "canon": {
            "resurrection_canon": true,
            "theotokos_canon": true,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "resurrection_then_menaion",
            "praises_stichera": {
                "total": 8,
                "resurrection": 4,
                "menaion": 4
            }
        },
        "great_doxology": true
    }'::jsonb, 30);

-- Rule 18: Polyeleos-rank on Weekday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (3, 'matins', FALSE,
    'Polyeleos-rank saint on weekday matins: saint troparion. Polyeleos sung. Canon from Octoechos + Menaion. Great Doxology.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["saint", "theotokos"]
        },
        "kathisma_hymns": {
            "source": "octoechos_and_menaion"
        },
        "polyeleos": true,
        "magnification": false,
        "canon": {
            "resurrection_canon": false,
            "theotokos_canon": true,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "menaion",
            "praises_stichera": {
                "total": 6,
                "resurrection": 0,
                "menaion": 6
            }
        },
        "great_doxology": true
    }'::jsonb, 30);

-- ---------------------------------------------------------------------------
-- RANK 4: Doxology-rank Saint - Matins
-- ---------------------------------------------------------------------------

-- Rule 19: Doxology-rank on Sunday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (4, 'matins', TRUE,
    'Doxology-rank saint on Sunday matins: resurrection and saint troparia. No polyeleos. Canon: resurrection + Theotokos + Menaion. Great Doxology sung.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["resurrection", "saint"]
        },
        "kathisma_hymns": {
            "source": "octoechos_and_menaion"
        },
        "polyeleos": false,
        "magnification": false,
        "canon": {
            "resurrection_canon": true,
            "theotokos_canon": true,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "resurrection_then_menaion",
            "praises_stichera": {
                "total": 8,
                "resurrection": 4,
                "menaion": 4
            }
        },
        "great_doxology": true
    }'::jsonb, 40);

-- Rule 20: Doxology-rank on Weekday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (4, 'matins', FALSE,
    'Doxology-rank saint on weekday matins: saint troparion. No polyeleos. Octoechos + Menaion canons. Great Doxology sung (the defining feature of this rank).',
    '{
        "god_is_the_lord": {
            "troparion_order": ["saint", "theotokos"]
        },
        "kathisma_hymns": {
            "source": "octoechos_and_menaion"
        },
        "polyeleos": false,
        "magnification": false,
        "canon": {
            "resurrection_canon": false,
            "theotokos_canon": true,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "menaion",
            "praises_stichera": {
                "total": 6,
                "resurrection": 0,
                "menaion": 6
            }
        },
        "great_doxology": true
    }'::jsonb, 40);

-- ---------------------------------------------------------------------------
-- RANK 5: Six-stichera Saint - Matins
-- ---------------------------------------------------------------------------

-- Rule 21: Six-stichera on Sunday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (5, 'matins', TRUE,
    'Six-stichera saint on Sunday matins: standard Sunday structure. Resurrection and saint troparia. No polyeleos. Canon: resurrection + Theotokos + Menaion. Great Doxology.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["resurrection", "saint", "theotokos"]
        },
        "kathisma_hymns": {
            "source": "octoechos_and_menaion"
        },
        "polyeleos": false,
        "magnification": false,
        "canon": {
            "resurrection_canon": true,
            "theotokos_canon": true,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "resurrection_then_menaion",
            "praises_stichera": {
                "total": 8,
                "resurrection": 4,
                "menaion": 4
            }
        },
        "great_doxology": true
    }'::jsonb, 50);

-- Rule 22: Six-stichera on Weekday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (5, 'matins', FALSE,
    'Six-stichera saint on weekday matins: saint troparion. No polyeleos. Octoechos + Menaion canons. Great Doxology is NOT sung (read instead); this distinguishes rank 5 from rank 4.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["saint", "theotokos"]
        },
        "kathisma_hymns": {
            "source": "octoechos_and_menaion"
        },
        "polyeleos": false,
        "magnification": false,
        "canon": {
            "resurrection_canon": false,
            "theotokos_canon": true,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "menaion",
            "praises_stichera": {
                "total": 4,
                "resurrection": 0,
                "menaion": 4
            }
        },
        "great_doxology": false
    }'::jsonb, 50);

-- ---------------------------------------------------------------------------
-- RANK 7: Ordinary Day - Matins
-- ---------------------------------------------------------------------------

-- Rule 23: Ordinary Sunday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (7, 'matins', TRUE,
    'Ordinary Sunday matins: full resurrection service. Troparia from Octoechos only. Canon: resurrection + Theotokos + Menaion. 8 praises (mostly resurrection). Great Doxology.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["resurrection", "resurrection", "theotokos"]
        },
        "kathisma_hymns": {
            "source": "octoechos"
        },
        "polyeleos": false,
        "magnification": false,
        "canon": {
            "resurrection_canon": true,
            "theotokos_canon": true,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "resurrection",
            "praises_stichera": {
                "total": 8,
                "resurrection": 5,
                "menaion": 3
            }
        },
        "great_doxology": true
    }'::jsonb, 70);

-- Rule 24: Ordinary Weekday - Matins
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, rule_description, assembly_logic, priority)
VALUES (7, 'matins', FALSE,
    'Ordinary weekday matins: saint troparion. No polyeleos. Octoechos + Menaion canons. Doxology read, not sung.',
    '{
        "god_is_the_lord": {
            "troparion_order": ["saint", "theotokos"]
        },
        "kathisma_hymns": {
            "source": "octoechos"
        },
        "polyeleos": false,
        "magnification": false,
        "canon": {
            "resurrection_canon": false,
            "theotokos_canon": true,
            "menaion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "octoechos",
            "praises_stichera": {
                "total": 4,
                "resurrection": 0,
                "menaion": 4
            }
        },
        "great_doxology": false
    }'::jsonb, 70);

-- =============================================================================
-- SATURDAY SPECIAL RULES
-- Saturday vespers (evening service) liturgically begins Sunday, so it uses
-- resurrection/Sunday material from the Octoechos of the coming tone.
-- =============================================================================

-- Rule 25: Saturday Evening Vespers (Ordinary - beginning of Sunday)
-- Note: is_saturday=TRUE here refers to the calendar day (Saturday evening),
-- while the liturgical content is that of Sunday. The is_sunday flag is FALSE
-- because the calendar day is Saturday; the assembly_logic contains Sunday
-- resurrection material.
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, is_saturday, rule_description, assembly_logic, priority)
VALUES (7, 'vespers', FALSE, TRUE,
    'Saturday evening vespers (ordinary): this is liturgically the beginning of Sunday. Uses resurrection stichera from the coming tone. 7 resurrection + 3 Menaion at Lord I Have Cried. Dogmatic Theotokion at Now-and-ever.',
    '{
        "lord_i_cried": {
            "total": 10,
            "resurrection": 7,
            "menaion": 3,
            "glory": "menaion_if_appointed",
            "now_and_ever": "dogmatic_theotokion"
        },
        "entrance": true,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory_now_and_ever": "octoechos_theotokion"
        },
        "troparion_order": ["resurrection"]
    }'::jsonb, 60);

-- Rule 26: Saturday Evening Vespers with Polyeleos+ Saint
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, is_saturday, rule_description, assembly_logic, priority)
VALUES (3, 'vespers', FALSE, TRUE,
    'Saturday evening vespers with polyeleos-rank saint on Sunday: 4 resurrection + 6 Menaion stichera. The saint commemorated is for Sunday.',
    '{
        "lord_i_cried": {
            "total": 10,
            "resurrection": 4,
            "menaion": 6,
            "glory": "menaion",
            "now_and_ever": "dogmatic_theotokion"
        },
        "entrance": true,
        "readings_count": 3,
        "aposticha": {
            "source": "octoechos",
            "count": 3,
            "glory": "menaion",
            "now_and_ever": "octoechos_theotokion"
        },
        "troparion_order": ["resurrection", "saint"]
    }'::jsonb, 25);

-- =============================================================================
-- LENTEN RULES
-- During Great Lent weekdays, the service structure changes significantly.
-- The Triodion supplements or replaces parts of the Octoechos. These rules
-- encode the most common Lenten weekday modifications.
-- =============================================================================

-- Rule 27: Lenten Weekday Vespers (ordinary saint, no major feast)
-- During Lent, weekday vespers omits the Little Entrance (even for ranks
-- that would normally have it). Stichera include Triodion material.
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, during_lent, rule_description, assembly_logic, priority)
VALUES (7, 'vespers', FALSE, TRUE,
    'Lenten weekday vespers: 3 Octoechos + 3 Menaion stichera at Lord I Have Cried. No entrance. Aposticha from the Triodion (Lenten stichera replace Octoechos aposticha). Concludes with Prayer of St. Ephraim.',
    '{
        "lord_i_cried": {
            "total": 6,
            "resurrection": 0,
            "octoechos": 3,
            "menaion": 3,
            "glory_now_and_ever": "triodion_theotokion"
        },
        "entrance": false,
        "aposticha": {
            "source": "triodion",
            "count": 3,
            "glory_now_and_ever": "triodion_theotokion"
        },
        "troparion_order": ["saint", "theotokos"],
        "prayer_of_ephraim": true
    }'::jsonb, 80);

-- Rule 28: Lenten Weekday Matins (ordinary)
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, during_lent, rule_description, assembly_logic, priority)
VALUES (7, 'matins', FALSE, TRUE,
    'Lenten weekday matins: "Alleluia" replaces "God is the Lord." Triodion tristichs instead of standard troparia. Canons from Octoechos, Menaion, and Triodion. Doxology read. Prayer of St. Ephraim.',
    '{
        "alleluia_service": true,
        "god_is_the_lord": {
            "replaced_by": "alleluia_with_triodion_tristichs"
        },
        "kathisma_hymns": {
            "source": "octoechos_and_triodion"
        },
        "polyeleos": false,
        "magnification": false,
        "canon": {
            "resurrection_canon": false,
            "theotokos_canon": true,
            "menaion_canon": true,
            "triodion_canon": true,
            "total_troparia_per_ode": 14
        },
        "after_canon": {
            "exapostilarion": "triodion",
            "praises_stichera": {
                "total": 4,
                "resurrection": 0,
                "menaion": 0,
                "triodion": 4
            }
        },
        "great_doxology": false,
        "prayer_of_ephraim": true
    }'::jsonb, 80);

-- Rule 29: Lenten Weekday Vespers with Polyeleos-rank Saint
-- A polyeleos-rank saint during Lent still receives enhanced treatment,
-- but Lenten modifications apply. The Entrance is restored for readings.
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, during_lent, rule_description, assembly_logic, priority)
VALUES (3, 'vespers', FALSE, TRUE,
    'Polyeleos-rank saint during Lent weekday vespers: 8 Menaion stichera (the saint overrides Octoechos). Entrance restored for 3 readings. Aposticha from Menaion. Prayer of St. Ephraim is omitted when polyeleos is served.',
    '{
        "lord_i_cried": {
            "total": 8,
            "resurrection": 0,
            "menaion": 8,
            "glory": "menaion",
            "now_and_ever": "menaion_theotokion"
        },
        "entrance": true,
        "readings_count": 3,
        "aposticha": {
            "source": "menaion",
            "count": 3,
            "glory": "menaion",
            "now_and_ever": "menaion_theotokion"
        },
        "troparion": "saint",
        "prayer_of_ephraim": false
    }'::jsonb, 25);

-- Rule 30: Holy Week override
-- During Holy Week, all Menaion/Octoechos combinations are suspended.
-- This rule acts as a sentinel; the application should use Triodion-only
-- services for Holy Week.
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, during_holy_week, rule_description, assembly_logic, priority)
VALUES (7, 'vespers', FALSE, TRUE,
    'Holy Week: all normal typikon combination rules are suspended. Services follow the Triodion exclusively. This sentinel rule instructs the application to bypass Octoechos/Menaion assembly entirely.',
    '{
        "override": "triodion_only",
        "note": "All services during Holy Week use the Triodion exclusively. No Octoechos or Menaion hymns are combined. Consult the Triodion directly for each day."
    }'::jsonb, 1);

-- Rule 31: Bright Week override
-- During Bright Week (Pascha through the Saturday before Thomas Sunday),
-- the Pentecostarion governs all services.
INSERT INTO typikon_rules (feast_rank, service_type, is_sunday, during_bright_week, rule_description, assembly_logic, priority)
VALUES (7, 'matins', FALSE, TRUE,
    'Bright Week: all normal typikon combination rules are suspended. Services follow the Pentecostarion exclusively. The Paschal canon is sung daily.',
    '{
        "override": "pentecostarion_only",
        "note": "During Bright Week, all services use Paschal material from the Pentecostarion. The Paschal canon replaces all other canons. No Octoechos or Menaion hymns are combined."
    }'::jsonb, 1);

-- =============================================================================
-- INDEXES for efficient rule lookup
-- =============================================================================

-- Index for the most common lookup pattern: finding rules by feast rank,
-- service type, and day-of-week flags
CREATE INDEX IF NOT EXISTS idx_typikon_rules_lookup
    ON typikon_rules (feast_rank, service_type, is_sunday, is_saturday, during_lent);

-- Index for priority-based ordering when multiple rules match
CREATE INDEX IF NOT EXISTS idx_typikon_rules_priority
    ON typikon_rules (priority, feast_rank);

-- =============================================================================
-- USAGE EXAMPLE (as a SQL comment for reference):
--
--   To find the correct rule for a given day:
--
--   SELECT assembly_logic
--   FROM typikon_rules
--   WHERE feast_rank = :rank
--     AND service_type = :service
--     AND is_sunday = :is_sunday
--     AND is_saturday = :is_saturday
--     AND during_lent = :during_lent
--     AND during_bright_week = :during_bright_week
--     AND during_holy_week = :during_holy_week
--   ORDER BY priority ASC
--   LIMIT 1;
--
--   If during_bright_week or during_holy_week is TRUE, the override rules
--   (priority=1) will take precedence over all other rules.
--
--   The returned JSONB assembly_logic is then interpreted by the application
--   layer to pull the correct hymn texts from the Octoechos and Menaion
--   tables and assemble them in the prescribed order.
-- =============================================================================
