-- ============================================================
-- ANTHOLOGION FEAST CALENDAR
-- Comprehensive Orthodox Christian Liturgical Calendar Data
-- ============================================================
--
-- This file populates the feasts table with fixed and moveable
-- feasts of the Orthodox Church, following the traditional
-- (Old Calendar / Julian) dates for fixed feasts.
--
-- Schema:
--   feast_name       - Full liturgical name of the feast
--   feast_type       - 'fixed' or 'moveable'
--   feast_month/day  - Calendar date for fixed feasts (NULL for moveable)
--   pascha_offset    - Days from Pascha for moveable feasts (NULL for fixed)
--   rank             - 1=Great Feast, 2=Vigil, 3=Polyeleos,
--                      4=Doxology, 5=Six Stichera, 6=Afterfeast, 7=Ordinary
--   saint_class      - Liturgical classification of the saint(s)
--   saint_names      - PostgreSQL array of commemorated names
--   has_custom_service - Whether a full proper service exists
--   metadata         - JSONB with troparion_tone, kontakion_tone, etc.
-- ============================================================

BEGIN;

-- ============================================================
-- SECTION 1: THE 12 GREAT FEASTS + PASCHA (rank 1)
-- These are the highest-ranking celebrations of the Church year.
-- ============================================================

-- Pascha: The Feast of Feasts, the Resurrection of our Lord
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Pascha - The Resurrection of our Lord Jesus Christ', 'moveable', NULL, NULL, 0, 1, NULL, ARRAY['Our Lord Jesus Christ'], TRUE, '{"troparion_tone": 5, "kontakion_tone": 8, "note": "Feast of Feasts, the center of the liturgical year"}'::jsonb);

-- 9 Fixed Great Feasts (in liturgical year order, starting September)

-- Nativity of the Theotokos: Beginning of the liturgical year's Great Feasts
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Nativity of the Most Holy Theotokos', 'fixed', 9, 8, NULL, 1, 'Theotokos', ARRAY['Most Holy Theotokos', 'Sts. Joachim and Anna'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 4, "forefeast": "Sept 7", "afterfeast_days": 4, "leavetaking": "Sept 12"}'::jsonb);

-- Exaltation of the Cross: Universal Exaltation of the Precious and Life-Giving Cross
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Universal Exaltation of the Precious and Life-Giving Cross', 'fixed', 9, 14, NULL, 1, 'Cross', ARRAY['The Precious Cross'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 4, "strict_fast": true, "forefeast": "Sept 13", "afterfeast_days": 7, "leavetaking": "Sept 21"}'::jsonb);

-- Entry of the Theotokos into the Temple
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Entry of the Most Holy Theotokos into the Temple', 'fixed', 11, 21, NULL, 1, 'Theotokos', ARRAY['Most Holy Theotokos'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 4, "forefeast": "Nov 20", "afterfeast_days": 4, "leavetaking": "Nov 25"}'::jsonb);

-- Nativity of Christ (Christmas)
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Nativity of our Lord God and Savior Jesus Christ', 'fixed', 12, 25, NULL, 1, NULL, ARRAY['Our Lord Jesus Christ'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3, "forefeast": "Dec 20", "afterfeast_days": 5, "leavetaking": "Dec 31"}'::jsonb);

-- Holy Theophany (Baptism of Christ)
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Theophany - Baptism of our Lord Jesus Christ', 'fixed', 1, 6, NULL, 1, NULL, ARRAY['Our Lord Jesus Christ'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 4, "forefeast": "Jan 2", "afterfeast_days": 8, "leavetaking": "Jan 14", "great_blessing_of_waters": true}'::jsonb);

-- Meeting of the Lord in the Temple (Presentation)
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Meeting of our Lord in the Temple', 'fixed', 2, 2, NULL, 1, NULL, ARRAY['Our Lord Jesus Christ', 'St. Simeon the God-Receiver', 'St. Anna the Prophetess'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 1, "afterfeast_days": 7, "leavetaking": "Feb 9"}'::jsonb);

-- Annunciation to the Theotokos
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Annunciation of the Most Holy Theotokos', 'fixed', 3, 25, NULL, 1, 'Theotokos', ARRAY['Most Holy Theotokos', 'Archangel Gabriel'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 8, "note": "Fish allowed even during Great Lent"}'::jsonb);

-- Transfiguration of our Lord
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Transfiguration of our Lord Jesus Christ', 'fixed', 8, 6, NULL, 1, NULL, ARRAY['Our Lord Jesus Christ'], TRUE, '{"troparion_tone": 7, "kontakion_tone": 7, "forefeast": "Aug 5", "afterfeast_days": 7, "leavetaking": "Aug 13"}'::jsonb);

-- Dormition of the Theotokos
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Dormition of the Most Holy Theotokos', 'fixed', 8, 15, NULL, 1, 'Theotokos', ARRAY['Most Holy Theotokos'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 2, "forefeast": "Aug 14", "afterfeast_days": 9, "leavetaking": "Aug 23", "dormition_fast": "Aug 1-14"}'::jsonb);

-- 3 Moveable Great Feasts

-- Palm Sunday: Entry of our Lord into Jerusalem
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Palm Sunday - Entry of our Lord into Jerusalem', 'moveable', NULL, NULL, -7, 1, NULL, ARRAY['Our Lord Jesus Christ'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 6, "note": "Fish allowed; branches blessed"}'::jsonb);

-- Ascension of our Lord
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Ascension of our Lord Jesus Christ', 'moveable', NULL, NULL, 39, 1, NULL, ARRAY['Our Lord Jesus Christ'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 6, "note": "Always falls on Thursday"}'::jsonb);

-- Pentecost: Descent of the Holy Spirit
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Pentecost - Descent of the Holy Spirit', 'moveable', NULL, NULL, 49, 1, NULL, ARRAY['The Holy Spirit'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 8, "note": "Kneeling prayers at Vespers"}'::jsonb);


-- ============================================================
-- SECTION 2: MAJOR MOVEABLE FEASTS (Triodion & Pentecostarion)
-- Arranged by pascha_offset from earliest to latest
-- ============================================================

-- Pre-Lenten Period (Triodion begins)
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Meatfare Sunday - Sunday of the Last Judgment', 'moveable', NULL, NULL, -56, 4, NULL, ARRAY[]::TEXT[], TRUE, '{"troparion_tone": 1, "note": "Last day for meat before Pascha"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Cheesefare Sunday - Forgiveness Sunday', 'moveable', NULL, NULL, -49, 4, NULL, ARRAY[]::TEXT[], TRUE, '{"troparion_tone": 6, "note": "Last day for dairy; Forgiveness Vespers"}'::jsonb);

-- Great Lent Sundays
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of Orthodoxy (First Sunday of Lent)', 'moveable', NULL, NULL, -42, 3, NULL, ARRAY[]::TEXT[], TRUE, '{"troparion_tone": 2, "note": "Triumph of Orthodoxy; procession of icons"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of St. Gregory Palamas (Second Sunday of Lent)', 'moveable', NULL, NULL, -35, 3, 'Heirarch', ARRAY['St. Gregory Palamas, Archbishop of Thessaloniki'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 8}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of the Veneration of the Cross (Third Sunday of Lent)', 'moveable', NULL, NULL, -28, 3, 'Cross', ARRAY['The Precious Cross'], TRUE, '{"troparion_tone": 1, "note": "Cross brought out for veneration"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of St. John Climacus (Fourth Sunday of Lent)', 'moveable', NULL, NULL, -21, 3, 'Monastic', ARRAY['St. John Climacus, Abbot of Sinai'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 4}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of St. Mary of Egypt (Fifth Sunday of Lent)', 'moveable', NULL, NULL, -14, 3, 'Nun', ARRAY['St. Mary of Egypt'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 3}'::jsonb);

-- Holy Week
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Lazarus Saturday', 'moveable', NULL, NULL, -8, 3, NULL, ARRAY['Righteous Lazarus'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 2, "note": "Fish allowed; foreshadowing of Resurrection"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Great and Holy Friday', 'moveable', NULL, NULL, -2, 2, NULL, ARRAY['Our Lord Jesus Christ'], TRUE, '{"note": "Strict fast - no food; 12 Passion Gospels at Matins; Vespers with Epitaphios"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Great and Holy Saturday', 'moveable', NULL, NULL, -1, 2, NULL, ARRAY['Our Lord Jesus Christ'], TRUE, '{"note": "15 OT readings at Vesperal Liturgy; descent into Hades"}'::jsonb);

-- Pentecostarion (Post-Pascha)
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Thomas Sunday - Antipascha', 'moveable', NULL, NULL, 7, 3, 'Apostle', ARRAY['Holy Apostle Thomas'], TRUE, '{"troparion_tone": 7, "kontakion_tone": 8, "note": "Renewal Sunday; touching of wounds"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of the Holy Myrrh-bearing Women', 'moveable', NULL, NULL, 14, 4, NULL, ARRAY['Holy Myrrh-bearing Women', 'Joseph of Arimathea', 'Nicodemus'], TRUE, '{"troparion_tone": 2, "kontakion_tone": 2}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of the Paralytic', 'moveable', NULL, NULL, 21, 4, NULL, ARRAY[]::TEXT[], TRUE, '{"troparion_tone": 3, "note": "Gospel of the healing at the Pool of Bethesda"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Mid-Pentecost', 'moveable', NULL, NULL, 24, 4, NULL, ARRAY[]::TEXT[], TRUE, '{"troparion_tone": 8, "kontakion_tone": 4, "note": "Wednesday - midpoint between Pascha and Pentecost"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of the Samaritan Woman', 'moveable', NULL, NULL, 28, 4, NULL, ARRAY['St. Photini the Samaritan Woman'], TRUE, '{"troparion_tone": 4, "note": "Gospel of Christ and the woman at the well"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of the Blind Man', 'moveable', NULL, NULL, 35, 4, NULL, ARRAY[]::TEXT[], TRUE, '{"troparion_tone": 5, "note": "Gospel of healing the man born blind"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Saturday of Souls before Pentecost', 'moveable', NULL, NULL, 48, 5, NULL, ARRAY[]::TEXT[], TRUE, '{"note": "Universal commemoration of the departed"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Monday of the Holy Spirit', 'moveable', NULL, NULL, 50, 3, NULL, ARRAY['The Holy Spirit'], TRUE, '{"troparion_tone": 8, "note": "Continuation of Pentecost; honor to the Holy Spirit"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sunday of All Saints', 'moveable', NULL, NULL, 56, 3, NULL, ARRAY['All Saints'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 8, "note": "Beginning of Apostles Fast; all saints known and unknown"}'::jsonb);


-- ============================================================
-- SECTION 3: SEPTEMBER - COMPLETE MONTH
-- All major commemorations for September (Old Calendar dates)
-- The liturgical year begins September 1.
-- ============================================================

-- Sept 1: Church New Year (Indiction) and St. Symeon Stylites
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Church New Year (Indiction)', 'fixed', 9, 1, NULL, 5, NULL, ARRAY[]::TEXT[], TRUE, '{"troparion_tone": 2, "kontakion_tone": 4, "note": "Beginning of the liturgical year"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Symeon Stylites', 'fixed', 9, 1, NULL, 5, 'Monastic', ARRAY['St. Symeon Stylites the Elder'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 2, "note": "First stylite, stood on pillar for 37 years"}'::jsonb);

-- Sept 2
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Martyr Mamas of Caesarea', 'fixed', 9, 2, NULL, 7, 'Martyr', ARRAY['St. Mamas of Caesarea'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 3}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('St. John the Faster, Patriarch of Constantinople', 'fixed', 9, 2, NULL, 7, 'Heirarch', ARRAY['St. John the Faster, Patriarch of Constantinople'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 4}'::jsonb);

-- Sept 3
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Hieromartyr Anthimus, Bishop of Nicomedia', 'fixed', 9, 3, NULL, 7, 'Hieromartyr', ARRAY['St. Anthimus, Bishop of Nicomedia'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 2}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Theoctistus, Fellow-ascetic of St. Euthymius', 'fixed', 9, 3, NULL, 7, 'Monastic', ARRAY['St. Theoctistus'], FALSE, '{"troparion_tone": 8}'::jsonb);

-- Sept 4
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Hieromartyr Babylas, Bishop of Antioch', 'fixed', 9, 4, NULL, 7, 'Hieromartyr', ARRAY['St. Babylas, Bishop of Antioch'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 4}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Prophet and God-seer Moses', 'fixed', 9, 4, NULL, 7, 'Prophet', ARRAY['Holy Prophet Moses'], FALSE, '{"troparion_tone": 2, "kontakion_tone": 2}'::jsonb);

-- Sept 5
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Prophet Zacharias and Righteous Elizabeth', 'fixed', 9, 5, NULL, 7, 'Prophet', ARRAY['Holy Prophet Zacharias', 'Righteous Elizabeth'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 4, "note": "Parents of St. John the Baptist"}'::jsonb);

-- Sept 6: Archangel Michael's Miracle at Colossae (Chonae)
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Miracle of the Archangel Michael at Colossae (Chonae)', 'fixed', 9, 6, NULL, 5, 'Angels', ARRAY['Archangel Michael'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2}'::jsonb);

-- Sept 7
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Forefeast of the Nativity of the Theotokos; Martyr Sozont of Cilicia', 'fixed', 9, 7, NULL, 7, 'Martyr', ARRAY['St. Sozont of Cilicia'], FALSE, '{"troparion_tone": 3, "note": "Forefeast of Sept 8"}'::jsonb);

-- Sept 8: GREAT FEAST (already inserted above in Section 1)

-- Sept 9
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Righteous Ancestors of God Joachim and Anna', 'fixed', 9, 9, NULL, 4, NULL, ARRAY['Righteous Joachim', 'Righteous Anna'], TRUE, '{"troparion_tone": 2, "kontakion_tone": 2, "note": "Afterfeast of Nativity of Theotokos; parents of the Virgin Mary"}'::jsonb);

-- Sept 10
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Martyresses Menodora, Metrodora, and Nymphodora', 'fixed', 9, 10, NULL, 7, 'Martyresses', ARRAY['St. Menodora', 'St. Metrodora', 'St. Nymphodora'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 4}'::jsonb);

-- Sept 11
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Theodora of Alexandria', 'fixed', 9, 11, NULL, 7, 'Nun', ARRAY['St. Theodora of Alexandria'], FALSE, '{"troparion_tone": 8, "kontakion_tone": 2}'::jsonb);

-- Sept 12: Leavetaking of Nativity of Theotokos
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Leavetaking of the Nativity of the Theotokos', 'fixed', 9, 12, NULL, 6, 'Theotokos', ARRAY['Most Holy Theotokos'], TRUE, '{"note": "Final day of the afterfeast period of the Nativity of the Theotokos"}'::jsonb);

-- Sept 13
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Forefeast of the Exaltation of the Cross', 'fixed', 9, 13, NULL, 7, 'Cross', ARRAY['The Precious Cross'], FALSE, '{"note": "Preparation for the Great Feast of the Cross"}'::jsonb);

-- Sept 14: GREAT FEAST (already inserted above in Section 1)

-- Sept 15
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Greatmartyr Niketas the Goth', 'fixed', 9, 15, NULL, 5, 'Martyr', ARRAY['St. Niketas the Goth'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2, "note": "Afterfeast of the Exaltation"}'::jsonb);

-- Sept 16
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Greatmartyr Euphemia the All-Praised', 'fixed', 9, 16, NULL, 4, 'Martyress', ARRAY['St. Euphemia the All-Praised'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 6, "note": "Her miracle confirmed the Orthodox faith at Chalcedon"}'::jsonb);

-- Sept 17
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Martyr Sophia and her three daughters Faith, Hope, and Love', 'fixed', 9, 17, NULL, 7, 'Martyresses', ARRAY['St. Sophia', 'St. Faith (Vera)', 'St. Hope (Nadezhda)', 'St. Love (Lyubov)'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 1}'::jsonb);

-- Sept 18
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('St. Eumenius, Bishop of Gortyna', 'fixed', 9, 18, NULL, 7, 'Heirarch', ARRAY['St. Eumenius, Bishop of Gortyna'], FALSE, '{"troparion_tone": 4}'::jsonb);

-- Sept 19
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Afterfeast of the Exaltation of the Cross', 'fixed', 9, 19, NULL, 6, 'Cross', ARRAY['The Precious Cross'], FALSE, '{"note": "Continuation of the afterfeast of the Cross"}'::jsonb);

-- Sept 20
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Greatmartyr Eustathius Placidas and family', 'fixed', 9, 20, NULL, 5, 'Martyr', ARRAY['St. Eustathius Placidas', 'St. Theopiste', 'Sts. Agapius and Theopistus'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2}'::jsonb);

-- Sept 21
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Leavetaking of the Exaltation of the Cross', 'fixed', 9, 21, NULL, 6, 'Cross', ARRAY['The Precious Cross'], TRUE, '{"note": "Final day of the afterfeast of the Exaltation"}'::jsonb);

-- Sept 22
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Hieromartyr Phocas, Bishop of Sinope', 'fixed', 9, 22, NULL, 7, 'Hieromartyr', ARRAY['St. Phocas, Bishop of Sinope'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 6}'::jsonb);

-- Sept 23: Conception of St. John the Baptist
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Conception of the Holy Glorious Prophet, Forerunner, and Baptist John', 'fixed', 9, 23, NULL, 3, 'St John Baptist', ARRAY['St. John the Baptist', 'Holy Prophet Zacharias', 'Righteous Elizabeth'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 1}'::jsonb);

-- Sept 24
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Protomartyr and Equal-to-the-Apostles Thecla', 'fixed', 9, 24, NULL, 5, 'Martyress', ARRAY['St. Thecla, Equal-to-the-Apostles'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 8, "note": "Disciple of Apostle Paul"}'::jsonb);

-- Sept 25
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Euphrosyne of Alexandria', 'fixed', 9, 25, NULL, 7, 'Nun', ARRAY['St. Euphrosyne of Alexandria'], FALSE, '{"troparion_tone": 8, "kontakion_tone": 2}'::jsonb);

-- Sept 26: Repose of Apostle and Evangelist John the Theologian
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Repose of the Holy Apostle and Evangelist John the Theologian', 'fixed', 9, 26, NULL, 2, 'Apostle', ARRAY['Holy Apostle and Evangelist John the Theologian'], TRUE, '{"troparion_tone": 2, "kontakion_tone": 2, "note": "Beloved disciple of Christ; author of Fourth Gospel, Epistles, and Revelation"}'::jsonb);

-- Sept 27
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Martyr Callistratus and his company', 'fixed', 9, 27, NULL, 7, 'Martyr', ARRAY['St. Callistratus', 'Forty-nine Martyrs'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 2}'::jsonb);

-- Sept 28
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Chariton the Confessor', 'fixed', 9, 28, NULL, 7, 'Monastic', ARRAY['St. Chariton the Confessor'], FALSE, '{"troparion_tone": 8, "kontakion_tone": 2, "note": "Founder of monasteries in Palestine"}'::jsonb);

-- Sept 29
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Cyriacus the Hermit', 'fixed', 9, 29, NULL, 7, 'Monastic', ARRAY['St. Cyriacus the Hermit'], FALSE, '{"troparion_tone": 1, "kontakion_tone": 2}'::jsonb);

-- Sept 30
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('St. Gregory the Illuminator, Enlightener of Armenia', 'fixed', 9, 30, NULL, 5, 'Heirarch', ARRAY['St. Gregory the Illuminator'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2, "note": "Brought Christianity to Armenia"}'::jsonb);


-- ============================================================
-- SECTION 4: ADDITIONAL MAJOR SAINTS THROUGHOUT THE YEAR
-- Significant commemorations from October through August
-- ============================================================

-- ---- OCTOBER ----

-- Oct 1: Protection (Pokrov) of the Theotokos
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Protection (Pokrov) of the Most Holy Theotokos', 'fixed', 10, 1, NULL, 2, 'Theotokos', ARRAY['Most Holy Theotokos'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3, "note": "Vision of St. Andrew the Fool at Blachernae"}'::jsonb);

-- Oct 6: Holy Apostle Thomas
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Apostle Thomas', 'fixed', 10, 6, NULL, 4, 'Apostle', ARRAY['Holy Apostle Thomas'], TRUE, '{"troparion_tone": 3, "kontakion_tone": 4, "note": "Preached in India"}'::jsonb);

-- Oct 18: Holy Apostle and Evangelist Luke
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Apostle and Evangelist Luke', 'fixed', 10, 18, NULL, 4, 'Apostle', ARRAY['Holy Apostle and Evangelist Luke'], TRUE, '{"troparion_tone": 5, "kontakion_tone": 2, "note": "Physician, companion of Apostle Paul, author of Gospel and Acts, iconographer"}'::jsonb);

-- Oct 26: Greatmartyr Demetrius of Thessaloniki
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Greatmartyr Demetrius the Myrrh-streamer of Thessaloniki', 'fixed', 10, 26, NULL, 3, 'Martyr', ARRAY['St. Demetrius of Thessaloniki'], TRUE, '{"troparion_tone": 3, "kontakion_tone": 2, "note": "Military saint; patron of Thessaloniki; myrrh streamed from his relics"}'::jsonb);

-- ---- NOVEMBER ----

-- Nov 1: Holy Unmercenaries Cosmas and Damian of Asia
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Unmercenaries and Wonderworkers Cosmas and Damian of Asia', 'fixed', 11, 1, NULL, 4, 'Unmercenaries', ARRAY['St. Cosmas', 'St. Damian'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 2, "note": "Healed the sick without accepting payment"}'::jsonb);

-- Nov 8: Synaxis of Archangel Michael and All Bodiless Powers
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Synaxis of the Archangel Michael and All the Bodiless Powers of Heaven', 'fixed', 11, 8, NULL, 2, 'Angels', ARRAY['Archangel Michael', 'Archangel Gabriel', 'Archangel Raphael', 'All Bodiless Powers'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2}'::jsonb);

-- Nov 13: St. John Chrysostom
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('St. John Chrysostom, Archbishop of Constantinople', 'fixed', 11, 13, NULL, 4, 'Heirarch', ARRAY['St. John Chrysostom, Archbishop of Constantinople'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 6, "note": "Author of the most-used Divine Liturgy; Golden-mouthed preacher"}'::jsonb);

-- Nov 14: Holy Apostle Philip
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Apostle Philip', 'fixed', 11, 14, NULL, 4, 'Apostle', ARRAY['Holy Apostle Philip'], TRUE, '{"troparion_tone": 3, "kontakion_tone": 8, "note": "Beginning of Nativity Fast (Nov 15)"}'::jsonb);

-- Nov 16: Holy Apostle and Evangelist Matthew
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Apostle and Evangelist Matthew', 'fixed', 11, 16, NULL, 4, 'Apostle', ARRAY['Holy Apostle and Evangelist Matthew'], TRUE, '{"troparion_tone": 3, "kontakion_tone": 4, "note": "Former tax collector; author of First Gospel"}'::jsonb);

-- Nov 25: Greatmartyr Catherine
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Greatmartyr Catherine of Alexandria', 'fixed', 11, 25, NULL, 4, 'Martyress', ARRAY['St. Catherine of Alexandria'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3, "note": "Patron of philosophers; debated 50 pagan philosophers"}'::jsonb);

-- Nov 30: Holy Apostle Andrew the First-Called
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Apostle Andrew the First-Called', 'fixed', 11, 30, NULL, 3, 'Apostle', ARRAY['Holy Apostle Andrew the First-Called'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2, "note": "First-called of the Apostles; patron of Constantinople and Ecumenical Patriarchate"}'::jsonb);

-- ---- DECEMBER ----

-- Dec 4: Greatmartyr Barbara
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Greatmartyr Barbara', 'fixed', 12, 4, NULL, 4, 'Martyress', ARRAY['St. Barbara'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 4, "note": "Patron saint of artillerymen and miners"}'::jsonb);

-- Dec 5: Venerable Sabbas the Sanctified
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Sabbas the Sanctified', 'fixed', 12, 5, NULL, 3, 'Monastic', ARRAY['St. Sabbas the Sanctified'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 8, "note": "Founder of Mar Saba monastery; compiled the Typikon"}'::jsonb);

-- Dec 6: St. Nicholas the Wonderworker
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('St. Nicholas the Wonderworker, Archbishop of Myra in Lycia', 'fixed', 12, 6, NULL, 3, 'Heirarch', ARRAY['St. Nicholas the Wonderworker, Archbishop of Myra'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3, "note": "One of most beloved saints; attended First Ecumenical Council"}'::jsonb);

-- Dec 12: St. Spyridon the Wonderworker
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('St. Spyridon the Wonderworker, Bishop of Trimythous', 'fixed', 12, 12, NULL, 4, 'Heirarch', ARRAY['St. Spyridon, Bishop of Trimythous'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 2, "note": "Shepherd-bishop who confounded Arius at Nicaea"}'::jsonb);

-- Dec 17: Holy Prophet Daniel and Three Holy Youths
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Prophet Daniel and the Three Holy Youths', 'fixed', 12, 17, NULL, 5, 'Prophet', ARRAY['Holy Prophet Daniel', 'Ananias', 'Azarias', 'Misael'], TRUE, '{"troparion_tone": 2, "kontakion_tone": 3}'::jsonb);

-- ---- JANUARY ----

-- Jan 1: St. Basil the Great / Circumcision of the Lord
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Circumcision of our Lord; St. Basil the Great, Archbishop of Caesarea', 'fixed', 1, 1, NULL, 2, 'Heirarch', ARRAY['Our Lord Jesus Christ', 'St. Basil the Great, Archbishop of Caesarea'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 4, "note": "Liturgy of St. Basil celebrated; author of monastic rule and liturgy"}'::jsonb);

-- Jan 7: Synaxis of St. John the Baptist
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Synaxis of the Holy Glorious Prophet, Forerunner, and Baptist John', 'fixed', 1, 7, NULL, 2, 'St John Baptist', ARRAY['St. John the Baptist and Forerunner'], TRUE, '{"troparion_tone": 2, "kontakion_tone": 6, "note": "Day after Theophany; honors the Baptizer of Christ"}'::jsonb);

-- Jan 17: Venerable Anthony the Great
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Anthony the Great', 'fixed', 1, 17, NULL, 3, 'Monastic', ARRAY['St. Anthony the Great'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2, "note": "Father of monasticism; lived in Egyptian desert"}'::jsonb);

-- Jan 18: Sts. Athanasius and Cyril of Alexandria
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sts. Athanasius and Cyril, Archbishops of Alexandria', 'fixed', 1, 18, NULL, 4, 'Heirarch', ARRAY['St. Athanasius the Great, Archbishop of Alexandria', 'St. Cyril, Archbishop of Alexandria'], TRUE, '{"troparion_tone": 3, "kontakion_tone": 4, "note": "Defenders of Orthodoxy against Arianism and Nestorianism"}'::jsonb);

-- Jan 25: St. Gregory the Theologian
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('St. Gregory the Theologian, Archbishop of Constantinople', 'fixed', 1, 25, NULL, 3, 'Heirarch', ARRAY['St. Gregory the Theologian, Archbishop of Constantinople'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 3, "note": "One of the Three Hierarchs; great orator on the Trinity"}'::jsonb);

-- Jan 27: Translation of Relics of St. John Chrysostom
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Translation of the Relics of St. John Chrysostom', 'fixed', 1, 27, NULL, 4, 'Heirarch', ARRAY['St. John Chrysostom'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 1}'::jsonb);

-- Jan 30: Three Holy Hierarchs
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Three Holy Hierarchs: Basil the Great, Gregory the Theologian, John Chrysostom', 'fixed', 1, 30, NULL, 2, 'Heirarch', ARRAY['St. Basil the Great', 'St. Gregory the Theologian', 'St. John Chrysostom'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 2, "note": "United feast established to end disputes over which was greatest"}'::jsonb);

-- ---- FEBRUARY ----

-- Feb 1: Martyr Tryphon
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Martyr Tryphon', 'fixed', 2, 1, NULL, 7, 'Martyr', ARRAY['St. Tryphon'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 8}'::jsonb);

-- Feb 12: Three Holy Hierarchs Afterfeast
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Afterfeast of the Three Holy Hierarchs; St. Meletius of Antioch', 'fixed', 2, 12, NULL, 6, 'Heirarch', ARRAY['St. Meletius, Archbishop of Antioch'], FALSE, '{"troparion_tone": 4}'::jsonb);

-- ---- MARCH ----

-- Mar 9: Forty Holy Martyrs of Sebastia
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Forty Holy Martyrs of Sebastia', 'fixed', 3, 9, NULL, 4, 'Martyrs', ARRAY['Forty Holy Martyrs of Sebastia'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 6, "note": "Soldiers frozen on lake; Liturgy of Presanctified Gifts always served"}'::jsonb);

-- Mar 17: Venerable Alexis, Man of God
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Alexis, Man of God', 'fixed', 3, 17, NULL, 7, 'Monastic', ARRAY['St. Alexis, Man of God'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 2}'::jsonb);

-- ---- APRIL ----

-- Apr 23: Holy Greatmartyr George the Trophy-Bearer
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Greatmartyr, Victory-Bearer, and Wonderworker George', 'fixed', 4, 23, NULL, 3, 'Martyr', ARRAY['St. George the Trophy-Bearer'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 4, "note": "Military saint; slayer of the dragon; patron of many nations"}'::jsonb);

-- Apr 25: Holy Apostle and Evangelist Mark
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Apostle and Evangelist Mark', 'fixed', 4, 25, NULL, 4, 'Apostle', ARRAY['Holy Apostle and Evangelist Mark'], TRUE, '{"troparion_tone": 3, "kontakion_tone": 2, "note": "Author of Second Gospel; founded Church of Alexandria"}'::jsonb);

-- ---- MAY ----

-- May 2: St. Athanasius the Great
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('St. Athanasius the Great, Archbishop of Alexandria', 'fixed', 5, 2, NULL, 4, 'Heirarch', ARRAY['St. Athanasius the Great, Archbishop of Alexandria'], TRUE, '{"troparion_tone": 3, "kontakion_tone": 2, "note": "Pillar of Orthodoxy; exiled five times for opposing Arianism"}'::jsonb);

-- May 8: Holy Apostle and Evangelist John the Theologian
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Apostle and Evangelist John the Theologian', 'fixed', 5, 8, NULL, 3, 'Apostle', ARRAY['Holy Apostle and Evangelist John the Theologian'], TRUE, '{"troparion_tone": 2, "kontakion_tone": 2, "note": "Second commemoration; manna appeared from his grave"}'::jsonb);

-- May 9: Translation of Relics of St. Nicholas
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Translation of the Relics of St. Nicholas to Bari', 'fixed', 5, 9, NULL, 4, 'Heirarch', ARRAY['St. Nicholas the Wonderworker'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3, "note": "Relics translated from Myra to Bari, Italy in 1087"}'::jsonb);

-- May 11: Sts. Cyril and Methodius, Equal-to-the-Apostles
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sts. Cyril and Methodius, Equal-to-the-Apostles, Enlighteners of the Slavs', 'fixed', 5, 11, NULL, 4, 'Heirarch', ARRAY['St. Cyril (Constantine)', 'St. Methodius'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3, "note": "Created Slavonic alphabet; translated Scripture and services"}'::jsonb);

-- May 21: Sts. Constantine and Helen, Equal-to-the-Apostles
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Sts. Constantine and Helen, Equal-to-the-Apostles', 'fixed', 5, 21, NULL, 3, NULL, ARRAY['St. Constantine the Great', 'St. Helen'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 3, "note": "Legalized Christianity; found the True Cross"}'::jsonb);

-- ---- JUNE ----

-- Jun 11: Holy Apostles Bartholomew and Barnabas
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Apostles Bartholomew and Barnabas', 'fixed', 6, 11, NULL, 4, 'Apostles', ARRAY['Holy Apostle Bartholomew', 'Holy Apostle Barnabas'], TRUE, '{"troparion_tone": 3, "kontakion_tone": 4}'::jsonb);

-- Jun 24: Nativity of the Holy Prophet, Forerunner, and Baptist John
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Nativity of the Holy Prophet, Forerunner, and Baptist John', 'fixed', 6, 24, NULL, 2, 'St John Baptist', ARRAY['St. John the Baptist and Forerunner'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3, "note": "Only saint whose nativity is celebrated as a major feast besides Christ and Theotokos"}'::jsonb);

-- Jun 29: Holy Prime-Apostles Peter and Paul
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Glorious and All-Praised Leaders of the Apostles, Peter and Paul', 'fixed', 6, 29, NULL, 2, 'Apostles', ARRAY['Holy Apostle Peter', 'Holy Apostle Paul'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2, "note": "End of Apostles Fast; leaders of the apostolic band"}'::jsonb);

-- Jun 30: Synaxis of the Holy Glorious Twelve Apostles
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Synaxis of the Holy Glorious and All-Praised Twelve Apostles', 'fixed', 6, 30, NULL, 4, 'Apostles', ARRAY['The Twelve Apostles'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2}'::jsonb);

-- ---- JULY ----

-- Jul 1: Holy Unmercenaries Cosmas and Damian of Rome
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Unmercenaries Cosmas and Damian of Rome', 'fixed', 7, 1, NULL, 4, 'Unmercenaries', ARRAY['St. Cosmas of Rome', 'St. Damian of Rome'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 2, "note": "Second pair of Unmercenary healers (distinct from Nov 1)"}'::jsonb);

-- Jul 2: Placing of the Robe of the Most Holy Theotokos at Blachernae
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Placing of the Robe of the Most Holy Theotokos at Blachernae', 'fixed', 7, 2, NULL, 3, 'Theotokos', ARRAY['Most Holy Theotokos'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 4}'::jsonb);

-- Jul 15: Holy Equal-to-the-Apostles Great Prince Vladimir
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Equal-to-the-Apostles Great Prince Vladimir, Enlightener of Rus', 'fixed', 7, 15, NULL, 3, NULL, ARRAY['St. Vladimir, Equal-to-the-Apostles'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 8, "note": "Baptized Rus in 988"}'::jsonb);

-- Jul 20: Holy Glorious Prophet Elijah (Elias)
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Glorious Prophet Elijah', 'fixed', 7, 20, NULL, 3, 'Prophet', ARRAY['Holy Prophet Elijah (Elias)'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2, "note": "Taken up to heaven in a chariot of fire; appeared at the Transfiguration"}'::jsonb);

-- Jul 25: Dormition of Righteous Anna, mother of the Theotokos
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Dormition of Righteous Anna, Mother of the Most Holy Theotokos', 'fixed', 7, 25, NULL, 4, NULL, ARRAY['Righteous Anna, Grandmother of Christ'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2}'::jsonb);

-- ---- AUGUST ----

-- Aug 1: Procession of the Cross / Beginning of Dormition Fast
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Procession of the Precious Cross; Beginning of the Dormition Fast', 'fixed', 8, 1, NULL, 5, 'Cross', ARRAY['The Precious Cross'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 4, "note": "Lesser blessing of water; beginning of Dormition fast"}'::jsonb);

-- Aug 2: Translation of Relics of Protomartyr Stephen
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Translation of the Relics of the Holy Protomartyr and Archdeacon Stephen', 'fixed', 8, 2, NULL, 4, 'Martyr', ARRAY['Holy Protomartyr and Archdeacon Stephen'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 6}'::jsonb);

-- Aug 7: Afterfeast of Transfiguration
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Afterfeast of the Transfiguration; Venerable Dometius', 'fixed', 8, 7, NULL, 6, NULL, ARRAY['St. Dometius of Persia'], FALSE, '{"note": "Afterfeast of Transfiguration"}'::jsonb);

-- Aug 29: Beheading of St. John the Baptist
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Beheading of the Holy Glorious Prophet, Forerunner, and Baptist John', 'fixed', 8, 29, NULL, 2, 'St John Baptist', ARRAY['St. John the Baptist and Forerunner'], TRUE, '{"troparion_tone": 2, "kontakion_tone": 5, "strict_fast": true, "note": "Strict fast day; one of the most solemn commemorations"}'::jsonb);


-- ============================================================
-- SECTION 5: ADDITIONAL NOTABLE FEASTS
-- Further entries to bring total above 100
-- ============================================================

-- Oct 14: Protection of the Theotokos (New Calendar) / St. Paraskeva
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Paraskeva of Serbia (Petka)', 'fixed', 10, 14, NULL, 5, 'Nun', ARRAY['St. Paraskeva (Petka) of Serbia'], TRUE, '{"troparion_tone": 8, "kontakion_tone": 3, "note": "Greatly venerated in the Balkans"}'::jsonb);

-- Oct 22: Kazan Icon of the Theotokos
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Kazan Icon of the Most Holy Theotokos', 'fixed', 10, 22, NULL, 4, 'Theotokos', ARRAY['Most Holy Theotokos'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 8}'::jsonb);

-- Nov 26: St. Alypius the Stylite
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Alypius the Stylite', 'fixed', 11, 26, NULL, 7, 'Monastic', ARRAY['St. Alypius the Stylite'], FALSE, '{"troparion_tone": 1, "kontakion_tone": 8}'::jsonb);

-- Dec 13: Repose of the Apostle Andrew (also Nov 30 above, this is different calendar tradition for some)
-- Holy Martyrs Eustratius, Auxentius, Eugene, Mardarius, and Orestes
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Martyrs Eustratius, Auxentius, Eugene, Mardarius, and Orestes', 'fixed', 12, 13, NULL, 5, 'Martyrs', ARRAY['St. Eustratius', 'St. Auxentius', 'St. Eugene', 'St. Mardarius', 'St. Orestes'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3}'::jsonb);

-- Dec 20: Forefeast of Nativity; Hieromartyr Ignatius the God-Bearer
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Forefeast of Nativity; Hieromartyr Ignatius the God-Bearer of Antioch', 'fixed', 12, 20, NULL, 5, 'Hieromartyr', ARRAY['St. Ignatius the God-Bearer, Bishop of Antioch'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3, "note": "Forefeast of Nativity begins; St. Ignatius was fed to lions in Rome"}'::jsonb);

-- Jan 10: St. Gregory of Nyssa
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('St. Gregory, Bishop of Nyssa', 'fixed', 1, 10, NULL, 5, 'Heirarch', ARRAY['St. Gregory, Bishop of Nyssa'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2, "note": "Cappadocian Father; brother of St. Basil"}'::jsonb);

-- Jan 14: Leavetaking of Theophany
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Leavetaking of Holy Theophany', 'fixed', 1, 14, NULL, 6, NULL, ARRAY[]::TEXT[], TRUE, '{"note": "Final day of the afterfeast of Theophany"}'::jsonb);

-- Feb 9: Leavetaking of Meeting of the Lord
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Leavetaking of the Meeting of the Lord', 'fixed', 2, 9, NULL, 6, NULL, ARRAY[]::TEXT[], TRUE, '{"note": "Final day of afterfeast of Meeting"}'::jsonb);

-- Mar 1: Venerable Eudocia
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Venerable Martyr Eudocia', 'fixed', 3, 1, NULL, 7, 'NunMartyr', ARRAY['St. Eudocia'], FALSE, '{"troparion_tone": 8, "kontakion_tone": 4}'::jsonb);

-- Apr 30: Holy Apostle James, son of Zebedee
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Apostle James, son of Zebedee', 'fixed', 4, 30, NULL, 4, 'Apostle', ARRAY['Holy Apostle James, son of Zebedee'], TRUE, '{"troparion_tone": 3, "kontakion_tone": 2, "note": "Brother of John the Theologian; first apostle martyred"}'::jsonb);

-- May 5: Greatmartyr Irene
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Greatmartyr Irene', 'fixed', 5, 5, NULL, 5, 'Martyress', ARRAY['St. Irene'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 3}'::jsonb);

-- Jun 1: Martyr Justin the Philosopher
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Martyr Justin the Philosopher', 'fixed', 6, 1, NULL, 7, 'Martyr', ARRAY['St. Justin the Philosopher (Justin Martyr)'], FALSE, '{"troparion_tone": 4, "kontakion_tone": 2, "note": "Early Christian apologist"}'::jsonb);

-- Jul 8: Greatmartyr Procopius
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Holy Greatmartyr Procopius', 'fixed', 7, 8, NULL, 5, 'Martyr', ARRAY['St. Procopius'], TRUE, '{"troparion_tone": 4, "kontakion_tone": 2}'::jsonb);

-- Jul 11: Great Martyr Euphemia
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Blessed Olga, Princess of Russia, Equal-to-the-Apostles', 'fixed', 7, 11, NULL, 5, NULL, ARRAY['St. Olga, Equal-to-the-Apostles'], TRUE, '{"troparion_tone": 1, "kontakion_tone": 4, "note": "First Russian ruler to be baptized"}'::jsonb);

-- Aug 13: Leavetaking of Transfiguration
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Leavetaking of the Holy Transfiguration', 'fixed', 8, 13, NULL, 6, NULL, ARRAY[]::TEXT[], TRUE, '{"note": "Final day of the afterfeast of Transfiguration"}'::jsonb);

-- Aug 23: Leavetaking of Dormition
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Leavetaking of the Dormition of the Theotokos', 'fixed', 8, 23, NULL, 6, 'Theotokos', ARRAY['Most Holy Theotokos'], TRUE, '{"note": "Final day of the afterfeast of Dormition"}'::jsonb);

-- Additional moveable feasts for completeness

-- Great Monday, Tuesday, Wednesday of Holy Week
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Great and Holy Monday', 'moveable', NULL, NULL, -6, 5, NULL, ARRAY[]::TEXT[], TRUE, '{"note": "Bridegroom Matins; commemoration of blessed Joseph and the barren fig tree"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Great and Holy Tuesday', 'moveable', NULL, NULL, -5, 5, NULL, ARRAY[]::TEXT[], TRUE, '{"note": "Bridegroom Matins; parable of the ten virgins"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Great and Holy Wednesday', 'moveable', NULL, NULL, -4, 5, NULL, ARRAY[]::TEXT[], TRUE, '{"note": "Bridegroom Matins; the sinful woman who anointed Christ; Holy Unction"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Great and Holy Thursday - Mystical Supper', 'moveable', NULL, NULL, -3, 2, NULL, ARRAY['Our Lord Jesus Christ'], TRUE, '{"note": "Vesperal Liturgy of St. Basil; institution of the Eucharist; 12 Gospels in evening"}'::jsonb);

-- Bright Week
INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Bright Monday', 'moveable', NULL, NULL, 1, 3, NULL, ARRAY[]::TEXT[], TRUE, '{"note": "Bright Week; Royal Hours not read; short services"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Bright Friday - Life-giving Spring of the Theotokos', 'moveable', NULL, NULL, 5, 3, 'Theotokos', ARRAY['Most Holy Theotokos'], TRUE, '{"troparion_tone": 4, "note": "Blessing of water; icon of the Life-giving Spring"}'::jsonb);

INSERT INTO feasts (feast_name, feast_type, feast_month, feast_day, pascha_offset, rank, saint_class, saint_names, has_custom_service, metadata)
VALUES ('Bright Saturday', 'moveable', NULL, NULL, 6, 3, NULL, ARRAY[]::TEXT[], TRUE, '{"note": "Final day of Bright Week"}'::jsonb);

COMMIT;

-- ============================================================
-- VERIFICATION QUERY (run to confirm data)
-- ============================================================
-- SELECT COUNT(*) AS total_feasts FROM feasts;
-- SELECT rank, COUNT(*) FROM feasts GROUP BY rank ORDER BY rank;
-- SELECT feast_type, COUNT(*) FROM feasts GROUP BY feast_type;
-- SELECT saint_class, COUNT(*) FROM feasts WHERE saint_class IS NOT NULL GROUP BY saint_class ORDER BY count DESC;
