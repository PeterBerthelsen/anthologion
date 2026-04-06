"""
Triodion Dictionary for Variables
"""

from _utils import regex_parse, format_text

triodion = {
    '-70': { #Sunday of the Publican & Pharisee
        'vespers': {
            'stichera_tone': 'Stichera from the Triodion, in Tone I:'
            ,'stichera': [
                'Brethren, let us not pray like the Pharisee: * for he who exalts himself shall be humbled. * Let us humble ourselves before God, * and with fasting cry aloud as did the Publican: * O God be merciful to us sinners.'
                ,'Brethren, let us not pray like the Pharisee: * for he who exalts himself shall be humbled. * Let us humble ourselves before God, * and with fasting cry aloud as did the Publican: * O God be merciful to us sinners.'
                ,'The Pharisee, overcome with vainglory, * and the Publican, bowed down in repentance, * approached Thee the only Master. * The one boasted and was deprived of blessings, * while the other kept silent and was found worthy of gifts. * Confirm me, O Christ God, * in these his cries of sorrow, * for Thou art the Lover of mankind.'
            ]
            ,'doxastichon':
                """
                In Tone VIII:
                Almighty Lord, I know how great is the power of tears. * For they led Hezekiah from the gates of death; * they delivered the sinful woman from the transgressions of many years; * they justified the Publican more than the Pharisee. ** And with all these I also pray: "Have mercy on me".
                """
            ,'aposticha_theotokion': 'Glory ..., in Tone V:\nMine eyes are weighed down by my transgressions, * and I cannot raise them on high, and see the height of heaven. * But receive me O Savior, for like the Publican I repent, ** and have mercy on me.\nNow & ever ..., in Tone V:\nThou art the temple and portal, * the palace and throne of the King, * O most honored Virgin, * through whom Christ the Lord, my Redeemer, * Who is the Sun of righteousness, * hath revealed Himself unto those who sleep in darkness, * deigning to enlighten those * whom He hath fashioned in His image by His own hand. * Wherefore, O all-hymned one, * as thou hast acquired a mother’s boldness before Him, ** entreat Him without ceasing, that our souls be saved.'
        }
        ,'matins': {
            'after50': 'In Tone VIII:\nGlory ..., The gates of repentance, do Thou open unto me, O Giver of Life, * for early in the morning my spirit seeketh Thy holy temple, * bearing the temple of my body all defiled. * But as One who art compassionate ** cleanse it by Thy loving-kindness and mercy. \nNow & ever ..., \nGuide me on the paths of salvation, O Theotokos: * for I have polluted my soul with shameful deeds * and wasted all my life in slothfulness. ** but by thine intercessions * do thou deliver me from all impurity. \nIn Tone VI: \nHave mercy upon me, O God, * according to Thy great mercy: * and according to the multitude of Thy compassion * blot out my transgressions. \nIn Tone VIII: \nAs I the wretched one ponder the multitude of evil deeds I have done, * I tremble for fear of the dread day of judgment. * But trusting in Thy compassionate mercy, * like David do I cry unto Thee: ** "Have mercy upon me, O God, according to Thy great mercy"'
            ,'canon': """
                ODE I
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: When Israel walked on foot in the sea as on dry land, * on seeing
                their pursuer Pharaoh drowned, * they cried: * Let us sing to God * a song
                of victory.
                Refrain: Have mercy on me, O God, have mercy on me.
                By parables Christ hath led all mankind to a life of amendment: Raising up
                the Publican from humbleness, he showed the Pharisee who exalted himself to
                be humbled.
                Refrain: Have mercy on me, O God, have mercy on me.
                From humility cometh an exalted honor, but from pride we see a grievous
                fall; let us, then, strive to emulate the good actions of the Publican, and hate the
                evil ones of the Pharisee.
                Refrain: Have mercy on me, O God, have mercy on me.
                Every good deed is rendered useless through pride, while every evil is
                cleansed by humility. Wherefore, let us in faith embrace humility, and utterly
                abhor the ways of vainglory.
                Refrain: Have mercy on me, O God, have mercy on me.
                The King of all, wishing His own disciples to be humble-minded, taught
                them to emulate the sighing of the Publican and his humility.
                Glory ..., I groan as did the Publican, and with never-silent lamentations O
                Lord I now draw near to Thy loving compassion, do Thou be merciful to me
                who doth now pass through life in humility.
                Now & ever ..., O lady, I dedicate to thee my understanding and my counsel,
                my expectation, my body, soul and spirit. From grievous adversaries and
                temptations, and from every threat to come, do thou deliver and save me.
                Katavasia: I shall open my mouth, * and be filled with the Spirit, * and
                utter discourse to the Queen and Mother; * and be seen radiantly keeping
                festival, * joyfully praising her wonders.
                ODE III
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: There is none as holy as Thou, * O Lord my God, * who hast
                exalted the horn of The faithful O good One, * and strengthened us upon
                the rock * of Thy confession.
                Refrain: Have mercy on me, O God, have mercy on me.
                From the dung-hill of the passions the humble are lifted up on high, while
                from the height of the virtues the high-minded suffer a grievous fall: let us flee
                such an image of wickedness.
                Refrain: Have mercy on me, O God, have mercy on me.
                Vainglory doth nullify the riches of righteousness, whereas humility
                scattereth a multitude of passions; bestowing this upon us, show us to be like the
                Publican O Savior.
                Refrain: Have mercy on me, O God, have mercy on me.
                Like the Publican let us also beat our breasts and cry out in compunction,
                “O God cleanse us sinners,” that like him we may receive forgiveness.
                Refrain: Have mercy on me, O God, have mercy on me.
                Zealously, O ye faithful, let us increase in meekness, and with humility let us
                live out the days of our lives in suffering of the heart, weeping and prayer, that
                we may receive forgiveness from God.
                Glory ..., Let us cast away, ye faithful, the high-minded boasting and hurtful
                pride of the Pharisee, and his most wicked, repugnant to God, malice.
                Now & ever ..., In thee, my only refuge, have I set my trust: let me not fall
                away from my good hope, but grant me thy protection, O pure One, and deliver
                me from every evil snare of my wicked enemies.
                Katavasia: O Theotokos, thou living and plentiful fount, * establish in
                spiritual fellowship those who sing hymns to thee, * and in thy divine
                glory * grant them crowns of glory.
                Sessional Hymns from the Triodion, in Tone IV:
                Humility exalted the Publican who was overcome with shame at his evil
                deeds, * when he cried to the Creator, “Be merciful:” * but exaltation brought
                down from righteousness the wretched Pharisee who spoke boastfully. *
                Therefore let us earnestly desire that which is good ** and avoid that which is
                evil.
                Glory ..., Of old humility exalted the Publican * who cried aloud with tears,
                * “Be merciful,” and he was justified. * Let us all follow his example, * for we
                have fallen into the depths of evil. * Let us cry to the Savior from the depths of
                our hearts: ** We have sinned, be merciful, O Thou Who alone lovest mankind.
                Now & ever ..., Be swift to receive our prayers, O Lady, * and bring them to
                thy Son and God, all-immaculate Sovereign Lady. * Deliver from tribulations
                those who flee to thee. * Destroy the wiles and subdue the arrogance ** of those
                who godlessly war against thy servants, O most pure One.
                ODE IV
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Christ is my power, * my God and my Lord, * the holy Church
                divinely singeth, * crying with a pure mind, * keeping festival in the Lord.
                Refrain: Have mercy on me, O God, have mercy on me.
                The Word, set an example showing that the path to exaltation is humility,
                having humbled Himself even unto taking the form of a servant, thereby
                instructing all, that he who humbleth himself shall be exalted on high.
                Refrain: Have mercy on me, O God, have mercy on me.
                The righteous Pharisee exalted himself and fell, wickedly rejecting humility,
                but through humility the Publican was exalted and justified.
                Refrain: Have mercy on me, O God, have mercy on me.
                He who was without need of virtue was deprived of them, and shown to be
                foolish. Yet the riches of humility justified him who was in most need of them,
                whose humility let us emulate.
                Refrain: Have mercy on me, O God, have mercy on me.
                O Lord, Thou didst forewarn all that Thou dost resist the high-minded, but
                grantest Thy grace to the humble. O savior send down now Thy grace upon us,
                for we have humbled ourselves.
                Glory ..., The Savior and Master, ever leading us to blessed exaltation, hath
                shown us that it is humility that raises one on high, for with His own hands He
                didst wash the feet of the disciples.
                Now & ever ..., O Virgin, who hast given birth to the unapproachable Light,
                by thy light-giving effulgence disperse the darkness of my soul, and taking me by
                the hand, guide my life into the path of salvation.
                Katavasia: He who sitteth in glory upon the throne of the Godhead, *
                Jesus the true God, * is come in a swift cloud * and with His sinless hands
                he hath saved those who cry: * Glory to Thy power, O Christ.
                ODE V
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Illumine with Thy divine light, I pray, O Good One, * the souls of
                those who with love rise early to pray to Thee, * that they may know Thee,
                O Word of God, * as the true God, * Who recalleth us from the darkness of
                sin.
                Refrain: Have mercy on me, O God, have mercy on me.
                Let us make haste to follow the Pharisee in his virtues and to emulate the
                Publican in his humility, and let us hate what is wrong in each of them: foolish
                opinion and the fall into self-destruction.
                Refrain: Have mercy on me, O God, have mercy on me.
                The righteousness of the Pharisee proved to be vain and was condemned,
                for it was yoked to prideful opinion; However the Publican became a cocompanion of humility, the virtue which exalts one on high.
                Refrain: Have mercy on me, O God, have mercy on me.
                The Pharisee thought to drive swiftly in the chariot of the virtues; but the
                Publican outran him on foot, for he had yoked humility to compassion.
                Refrain: Have mercy on me, O God, have mercy on me.
                Pondering with our minds the parable of the Publican, let us all emulate him
                with tears, offering to God a contrite spirit, seeking the remission of our sins.
                Glory ..., Let us cast far away the wicked haughtiness and boasting of the
                Pharisee, that we may not be stripped of divine grace.
                Now & ever ..., A staff of strength grant unto all, O good one, who flee
                unto thee, grant them victory in the midst of all enemies and deliver them from
                every evil circumstance.
                Katavasia: All creation stands in awe of thy divine glory; * for thou, O
                Virgin who hast not known wedlock, * didst contain within thy womb the
                God of all, * and gave birth to the timeless Son, * bestowing peace, upon
                all who hymn thee.
                ODE VI
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Beholding the sea of life surging with the tempest of temptations, *
                I run to Thy calm haven, and cry to Thee: * Raise up my life from
                corruption, * O Most Merciful One.
                Refrain: Have mercy on me, O God, have mercy on me.
                The Publican along with the Pharisee ran the race of life, but the one was
                overcome by high-mindedness and shipwrecked, while the other was saved by
                humility.
                Refrain: Have mercy on me, O God, have mercy on me.
                Changing to a humble course of life, let us emulate the fervent wisdom of
                the Publican and flee the deadening conceit of the Pharisee; and we shall live.
                Refrain: Have mercy on me, O God, have mercy on me.
                Let us fervently follow the ways of Jesus the Savior and His humility, if we
                desire to reach the tabernacle of everlasting joy and to dwell in the land of the
                living.
                Refrain: Have mercy on me, O God, have mercy on me.
                O Master, Thou hast shown to Thy disciples the humility that raiseth men
                on high, for girding Thy loins with a towel, and washing their feet Thou didst
                prepare them to follow Thine example.
                Glory ..., The Pharisee passed his life in virtue and the Publican in sin; but
                the former was brought low by his pride, while the latter was raised on high by
                his humble-mindedness.
                Now & ever ..., I was formed naked in innocence and simplicity; but the
                enemy hath clothed me in the raiment of transgressions and the grossness of the
                flesh. But by thine intercessions, O Maiden, I have been saved.
                Katavasia: Celebrating the divine and solemn feast * of the Mother of God
                * O ye divinely wise, * let us come, clapping our hands, * and glorify God
                who was born of her.
                Kontakion from the Triodion, in Tone IV
                Let us flee from the proud-speaking of the Pharisee * and learn from the
                Publican the loftiness of words of humility, * and with penitential lamentation let
                us cry aloud: “O Savior of the world ** be merciful to us, and cleanse us Thy
                servants’.
                Ikos : Let us all humble ourselves, brethren; sighing and lamenting, beating
                our conscience, that at the eternal judgment we may be numbered with the
                faithful and the righteous, and receive forgiveness. Let us pray that we behold the
                place truly peaceful, where there is neither pain, nor sorrow, nor sighing from the
                soul, in the wondrous Eden fashioned by Christ, for He is God coeternal with
                the Father.
                SYNAXARION READING:
                With God, on this present day we begin the Triodion, the hymns of which
                were composed by many of our holy and God-bearing Fathers, inspired by the
                Holy Spirit according to their worthiness. The first of all was the great author
                Cosmas of Maiuma, who composed the three odes (symbolic of the Holy and
                Life-Creating Trinity) for the Great and Holy Week of the Passion of our Lord
                and God and Savior Jesus Christ. After him others of the Fathers, including
                Theodore and Joseph of the Studite Monastery, following his zealous example,
                arranged the services of the other weeks of the Holy and Great Forty-day Fast,
                reserving them at first for the use of the Studite Monastery. Furthermore they
                composed and arranged hymns, seeking them and collecting them from other
                books of the Fathers. Since, according to the Triodion, Sunday, the celebration
                of the Resurrection, is the first day of the week as well as the last or eighth day,
                they prescribed the first ODE of the canon to be sung on the second day of the
                week, i.e. Monday. The second ODE was prescribed for Tuesday, the third day
                of the week, the third ODE for Wednesday, the fourth ODE for Thursday, the
                fifth ODE for Friday, and the sixth and seventh ODES for Saturday. The rest,
                the eighth and ninth ODES, are prescribed for every day. It must be known,
                however, that although it is called the Triodion, it does have services with other
                than three-ODE canons. It is so named because the majority of the services have
                three ODE canons, especially during Holy Week. For it was our Holy Fathers’
                idea that through the entire Triodion would be commemorated in a concise form
                all God’s benefits to us from the beginning, using it as a reminder for all of us
                that we were created by Him, and were exiled from Paradise through the tasting
                of the fruit, rejecting the commandment that was given to us for our knowledge,
                and we were cast out through the envy of the arch villain serpent and enemy,
                who was made to crawl for his arrogance. That we remained cut off from the
                benefits of Paradise and were led by the devil. That the Son and Word of God,
                having suffered in His mercy, bowing the heavens, descended and made His
                abode in the Virgin and became man for our sake, showing us through His life
                the ascent into the heavens, through humility first of all then fasting and the
                rejection of evil and through His other deeds. That He suffered and rose from
                the dead and ascended once more into heaven, and He sent down the Holy Spirit
                upon His holy disciples and Apostles, who all proclaimed Him to be the Son of
                God and the most perfect God. And that once more the divine Apostles acted
                through the grace of the most Holy Spirit and gathered all the saints from the
                ends of the earth through their preaching, filling the world on high, which was
                the intention of the Creator from the beginning. Now the purpose of the
                Triodion intended by the Holy Fathers on these three present feasts of the
                Publican and the Pharisee, the Prodigal Son, and the Second Coming is a kind of
                preparatory lesson and stimulation to prepare ourselves for the spiritual labors of
                the Fast, having put aside our usual corrupt habits. First of all they present to us
                the parable of the Publican and the Pharisee, and they call the week following
                precursory. For those who desire to go off to do military battle, first ascertain the
                time of the battle from the leaders, so that having cleaned and polished their
                weapons, and preparing well all their other matters, and having removed all
                obstacles from their path, they earnestly go forth to their labors, taking the
                necessary supplies. Often before battle they tell anecdotes and tales and parables
                to incite their hearts to zeal, driving off idleness, fear, despair and other
                inadequate feelings. So the divine Fathers herald the coming fast against the
                armies of demons as a passion which holds fast our souls to cleanse ourselves of
                the poison accumulated over a long period of time. Not yet possessing those
                benefits, let us strive to obtain them, and arming ourselves properly, so let us set
                off to the labors of the Fast. Now the first weapon among the virtues is
                repentance and humility. And the temptation to attain the greatest humility is
                pride and arrogance. So they place before us first of all this present trustworthy
                parable from the Divine Gospel. It encourages us to shun the desire for the pride
                and arrogance of the Pharisee, and to cultivate the opposite desire of the
                Publican for humility and repentance. For the greatest and most grievous passion
                is pride and arrogance, since this is how the Devil fell from the heavens before
                the morning star and was cast into darkness. Because of this Adam, the father of
                our race, was driven from Paradise through partaking of the fruit. Through this
                example the Holy Fathers encourage all not to be proud of their successes, but
                always to be humble. For the Lord sets Himself against the proud, but He gives
                grace to the humble. Better a man who has sinned, if he knows that he has
                sinned and repents, than a man who has not sinned and thinks of himself as
                righteous. For Christ said, “I say to you that the Publican went down to his
                house justified rather than the Pharisee.” This parable reveals that no one should
                exalt himself, even though he has done good deeds, but rather should always be
                humble and pray from his heart to God, for even if he should fall into the most
                serious sin, salvation is not far off
                Through the prayers of all Thy holy Hymnographers,
                O Christ our God, have mercy on us. Amen.
                ODE VII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: An Angel made the furnace bedew the holy Children. * But the
                command of God consumed the Chaldeans * and prevailed upon the
                tyrant to cry: * O God of our fathers, Blessed art Thou.
                Refrain: Have mercy on me, O God, have mercy on me.
                Exalted by the works of self-justification, the Pharisee was grievously snared
                in the nets of vainglory, boasting madly; but the Publican was lifted on high on
                the light wings of humility, and drew near to God.
                Refrain: Have mercy on me, O God, have mercy on me.
                Using humility as a ladder, the Publican was raised on high to the heights of
                heaven; but by the putrid foolishness of pride the wretched Pharisee fell into the
                abyss of Hades.
                Refrain: Have mercy on me, O God, have mercy on me.
                The enemy doth catch the righteous and despoil them through vainglory,
                blinding sinners in the nets of despair. But let us emulate the Publican and hasten
                to escape from both these evils.
                Refrain: Have mercy on me, O God, have mercy on me.
                In our prayer before God, let us fall down with tears and fervent sighs,
                emulating the Publican in his lofty humility; and singing in faith: “O God of our
                fathers, blessed art Thou”.
                Glory ..., Thou hast forewarned Thy disciples, O Master, teaching them not
                to be lofty of wisdom, but to be numbered with those who are humble-minded.
                Therefore, O Savior, in faith we cry aloud to Thee: O God of our fathers,
                blessed art Thou.
                Now & ever ..., O thou beauty of Jacob, divine Ladder which of old he
                beheld stretching from earth to heaven, thou holy Virgin, who hath brought
                down from on high God made flesh, and doth bring mortal man up to heaven.
                Katavasia: Refusing to worship created things * in place of the Creator, *
                the divinely wise youths bravely trampled down the threatening fire * and
                rejoicing they sang aloud: * O supremely hymned Lord and God of our
                Fathers, Blessed art Thou.
                ODE VIII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Thou didst make flame bedew the holy children, * and didst burn
                the sacrifice of a righteous man with water. * For Thou alone, O Christ,
                dost do all as Thou willest, * Thee do we exalt throughout all ages.
                Refrain: Have mercy on me, O God, have mercy on me.
                The humble-minded sighing of the Publican found the mercy of the Lord,
                and he was saved; but by the evil tongue of boasting, the Pharisee fell from
                righteousness.
                Refrain: Have mercy on me, O God, have mercy on me.
                O ye faithful, let us avoid the self-will of the Pharisee; who called himself
                pure, rather let us strive to emulate the Publican’s goodness, who gained
                forgiveness with humility.
                Refrain: Have mercy on me, O God, have mercy on me.
                O ye faithful, let us utter the words of the Publican in the holy temple,
                “God be merciful,” that with him we may obtain forgiveness, and be delivered
                from the vile boasting of the Pharisee.
                Refrain: Have mercy on me, O God, have mercy on me.
                Let us all emulate the sighing of the Publican and, speaking to God with
                warm tears, let us cry out: “O Lover of mankind, we have sinned, but in Thy
                merciful compassion, do Thou cleanse and save us.”
                Refrain: Let us bless the Father, Son, and Holy Spirit, the Lord!
                God accepted the groaning of the Publican and having justified him, hath
                shown unto us all, that He is quickly turned to compassion by the sighings and
                tears of those who ask for the forgiveness of sins.
                Now & ever ..., I know of no other intercessor save thee, I offer thee, O
                pure and all-immaculate One, as my mediator before Him Whom thou didst
                bear. Do thou show me to be free from all that doth grieve me.
                Refrain: We praise, bless and worship the Lord, chanting and supremely
                exalting Him throughout all ages.
                Katavasia: The Offspring of the Theotokos * saved the holy children in the
                furnace. * He who was then prefigured hath now been born on earth, *
                and He gathereth all creation to hymn thee: * all ye works praise ye the
                Lord * and supremely exalt Him throughout all ages.
                And then we chant the Hymn of the Most Holy Theotokos (the Magnificat)
                ODE IX
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: It is impossible for mankind to see God * upon Whom the orders
                of Angels dare not gaze; * but through thee, O all-pure one, * did the
                Word Incarnate become a man * and with the Heavenly Hosts * Him we
                magnify and thee we call blessed.
                Refrain: Have mercy on me, O God, have mercy on me.
                Christ hath set before us as a path to exaltation and an image of salvation,
                the humility of the Publican: which, let us strive after by rejecting disdainful pride
                and gaining God’s mercy through humble-mindedness.
                Refrain: Have mercy on me, O God, have mercy on me.
                Let us cast away pride and learn the righteousness of the humble-minded;
                let us not seek to justify ourselves, but rather let us abhor the delusion of
                vainglory, and with the Publican let us pray to God.
                Refrain: Have mercy on me, O God, have mercy on me.
                Let us offer the Creator entreaties for mercy, as did the Publican,. Let us
                avoid the ungrateful prayers of the Pharisee and the boastful words with which
                he judged his neighbor, that we may gain God’s mercy and light.
                Refrain: Have mercy on me, O God, have mercy on me.
                Weighed down by a great multitude of sins, I have surpassed the Publican in
                an excess of evil, having embraced the self-adulating madness of the Pharisee,
                wherefore I am utterly devoid of all that is good: O Lord, spare me.
                Refrain: Have mercy on me, O God, have mercy on me.
                O Lord, grant blessedness to those who for Thy sake are poor in spirit, and
                who follow Thy teachings, bringing unto Thee a contrite heart. Receive and save
                them who worship Thee.
                Glory ..., May we never pray unto Thee as did the Pharisee, may we enter
                the Temple justified by sighing and tears, with a heart that is broken and
                humbled, laying aside the heavy yoke of sin and thus be cleansed.
                Now & ever ..., Grant us to hymn, glorify, and bless thee, to worthily honor
                thee, O most pure one; glorifying thy birth-giving, O only-blessed one, for thou
                art the praise of Orthodox Christians, and their divinely-acceptable intercessor
                before God
                Katavasia: Let every mortal born on earth, * radiant with light, in spirit
                leap for joy; * and let the host of the angelic powers * celebrate and honor
                the holy feast of the Mother of God, * and let them cry aloud: * Rejoice! O
                Theotokos, thou pure Ever-Virgin.
            """
            ,'exapostilarion': 'Glory ..., in Tone III: Let us flee from the wicked boasting of the Pharisee, * and learn the noble humility of the Publican, * that we may be exalted and cry aloud with him unto God: * Be merciful unto Thy servants, O Christ our Savior, * Who wast willingly born from a Virgin, * who hast endured the Cross and with Thyself raised up the world ** by Thy divine power. Now & ever ..., Theotokion: The Maker of creation and the God of all, * took flesh from thine undefiled womb, O all-hymned Theotokos, * renewing the whole of my corrupted nature. * As thou wast before childbirth, * so wast thou left after childbirth. * Therefore we all praise thee with faith ** and we cry: Rejoice! Glory of the world.'
            ,'aposticha':
                """
                4 Resurrection Stichera, in the Tone of the week:
                Then 4 Stichera from the Triodion, in Tone VI:
                Verse: Praise Him with timbrel and dance, * praise him with strings and
                flute.
                Brethren, let us not pray like the Pharisee: * for he who doth exalt himself
                shall be humbled. * Let us humble ourselves before God, * and with fasting cry
                aloud as did the Publican: * “God be merciful to us sinners”.
                Verse: Praise Him with tuneful cymbals, praise Him with cymbals of
                jubilation. * Let every breath praise the Lord.
                In Tone III: Understand, O my soul, the difference between the Publican
                and the Pharisee, * hate the haughty words of the one, and eagerly imitate the
                contrite prayer of the other, crying aloud: ** “O God cleanse me a sinner and
                have mercy on me”.
                \nVerse: I will confess Thee, O Lord, with my whole heart, * I will tell of
                all Thy wonders.
                The Pharisee, overcome with vainglory, * and the Publican, bowed down in
                repentance, * approached Thee the only Master. * The one boasted and was
                deprived of blessings, * while the other kept silent and was found worthy of gifts.
                * Confirm me, O Christ God, * in these his cries of sorrow, ** for Thou art the
                Lover of mankind.
                Verse: I will be glad and rejoice in Thee, I will chant unto Thy name, O
                Most High.
                O ye faithful, let us hate the boastful words of the Pharisee * and emulate
                the contrite prayer of the Publican. * Let us not think proud thoughts, but
                humbling ourselves in contrition let us cry: ** God be merciful to our sins.
                """
            ,'aposticha_theotokion':
                """
                Glory ..., in Tone VIII:
                O Lord, Thou hast condemned the Pharisee * who justified himself by
                boasting of his works, * and Thou hast justified the Publican who humbled
                himself * and with cries of sorrow begged for mercy. * For Thou dost reject
                proud-minded thoughts, * but dost not despise a contrite heart. * Therefore
                humbled we fall down before Thee * who hast suffered for our sake: ** Grant us
                forgiveness and great mercy.
                Now & ever ..., in Tone II:
                Most Blessed art Thou, O Virgin Theotokos, * for through Him Who
                became incarnate of thee is Hades led captive, * Adam recalled, the curse
                annulled, Eve set free, death slain, * and we are given life. Wherefore, we cry
                aloud in praise: * Blessed art Thou, O Christ God, ** Who hast been thus wellpleased, glory to Thee.
                """

        }
        ,'liturgy': {
            'beatitudes': [
                'The Publican along with the Pharisee ran the race of life, but the one was overcome by high-mindedness and shipwrecked, while the other was saved by humility.'
                ,'Changing to a humble course of life, let us emulate the fervent wisdom of the Publican and flee the deadening conceit of the Pharisee; and we shall live.'
                ,'Glory ..., The Pharisee passed his life in virtue and the Publican in sin; but the former was brought low by his pride, while the latter was raised on high by his humble-mindedness.'
                ,'Now & ever ..., I was formed naked in innocence and simplicity; but the enemy hath clothed me in the raiment of transgressions and the grossness of the flesh. But by thine intercessions, O Maiden, I have been saved.'
            ]
            ,'kontakion': 'Kontakion in Tone IV:\nLet us flee from the proud speaking of the Pharisee * and learn the humility of the Publican, * and with groaning let us cry unto the Savior: * Be merciful to us, ** for Thou alone art ready to forgive. '
            ,'readings':
                """
                2nd EPISTLE TO TIMOTHY: (3:10-15)
                My Child Timothy: Thou hast fully known my doctrine, manner of life,
                purpose, faith, longsuffering, charity, patience, Persecutions, afflictions, which
                came unto me at Antioch, at Iconium, at Lystra; what persecutions I endured:
                but out of them all the Lord delivered me. Yea, and all that will live godly in
                Christ Jesus shall suffer persecution. But evil men and seducers shall wax worse
                and worse, deceiving, and being deceived. But continue thou in the things which
                thou hast learned and hast been assured of, knowing of whom thou hast learned
                them; And that from a child thou hast known the holy scriptures, which are able
                to make thee wise unto salvation through faith which is in Christ Jesus
                Alleluia in the Tone of the week:
                GOSPEL ACCORDING TO ST. LUKE 18:10-14
                The Lord spake a parable saying: Two men went up into the temple to pray;
                the one a Pharisee, and the other a publican. The Pharisee stood and prayed thus
                with himself, God, I thank thee, that I am not as other men are, extortioners,
                unjust, adulterers, or even as this publican. I fast twice in the week, I give tithes
                of all that I possess. And the publican, standing afar off, would not lift up so
                much as his eyes unto heaven, but smote upon his breast, saying, God be
                merciful to me a sinner. I tell you, this man went down to his house justified
                rather than the other: for every one that exalteth himself shall be abased; and he
                that humbleth himself shall be exalted.
                """
        }
    }
    ,'-63': { #Sunday of the Prodigal Son
        'vespers': {
            'stichera_tone': 'In Tone I:'
            ,'stichera': [
                'I was entrusted with a sinless and living land, * but having sowed with sin, I have reaped with a sickle, the ears of slothfulness; * in thick sheaves I garnered my actions * but winnowed them not on the threshing floor of repentance. * But I pray Thee, O my God, the pre-eternal husbandman, * with the wind of Thy loving-kindness winnow the chaff of my works, * and grant unto my soul the wheat of forgiveness; ** do Thou shut me in Thy heavenly storehouse and save me.'
                ,'I was entrusted with a sinless and living land, * but having sowed with sin, I have reaped with a sickle, the ears of slothfulness; * in thick sheaves I garnered my actions * but winnowed them not on the threshing floor of repentance. * But I pray Thee, O my God, the pre-eternal husbandman, * with the wind of Thy loving-kindness winnow the chaff of my works, * and grant unto my soul the wheat of forgiveness; ** do Thou shut me in Thy heavenly storehouse and save me.'
                ,'Brethren, let us fathom the meaning of this mystery. * For when the Prodigal Son fled back to his father’s home, the good Father came out to meet him and kissed him, * giving to the Prodigal son once again his former glory, * and mystically rejoicing on high, he sacrificed the fatted calf. * Let our lives, then, be worthy of the man-befriending Father Who hath offered sacrifice, ** and of the glorious Victim, the Savior of our souls.'
                ,'Brethren, let us fathom the meaning of this mystery. * For when the Prodigal Son fled back to his father’s home, the good Father came out to meet him and kissed him, * giving to the Prodigal son once again his former glory, * and mystically rejoicing on high, he sacrificed the fatted calf. * Let our lives, then, be worthy of the man-befriending Father Who hath offered sacrifice, ** and of the glorious Victim, the Savior of our souls.'
            ]
            ,'doxastichon': 'O great are the blessings, which in my wretchedness I have deprived myself! * I have fallen from the kingdom in my misery! * I have wasted the riches given me, * I have transgressed the commandments. * Woe is me O my soul! Thou art henceforth condemned to the eternal fire. * Wherefore before the end cry out to Christ God: ** Receive me as the Prodigal Son, O God, and have mercy on me.'
            ,'aposticha_theotokion': ' Glory ..., in Tone VI: \n I have wasted the wealth which the Father hath given me, * and in my wretchedness I have fed with the dumb beasts, * Yearning for their food, I remained hungry and without my fill. * But I now return to the compassionate Father and cry out with tears: * I fall down before Thy loving-kindness, ** receive me as a hired servant and save me. \n Now & ever ..., in Tone VI: \n Christ the Lord, my Creator and Redeemer, * Who came forth from thy womb, O most pure one, * and clothed Himself in my nature, * hath freed Adam from the primal curse. * Wherefore, like the angel * we unceasingly cry out to thee, O all-pure one, * who art truly the Mother of God and Virgin: * Rejoice!, O Sovereign Lady, ** the intercession, protection and salvation for our souls!'
        } #Vespers
        ,'matins': {
            'polyeleos':"""
                By the waters of Babylon, there we sat down and we wept when we remembered Zion. Alleluia.
                Upon the Willows in the midst thereof did we hang our instruments. Alleluia.
                For there, they that had taken us captive asked us for Words of song. Alleluia.
                And they that had led us away asked us for a hymn, saying: Sing us one of the songs of Zion. Alleluia.
                How shall we sing the Lord’s song in a strange land? Alleluia.
                If I forget thee, O Jerusalem, let my right hand be forgotten. Alleluia.
                Let my tongue cleave to my throat, if I remember thee not, Alleluia.
                If I set not Jerusalem above all other, as at the head of my joy. Alleluia.
                Remember, O Lord, the sons of Edom, in the day of Jerusalem, Alleluia.
                Who said: Lay waste, lay waste to her, even to the foundations thereof. Alleluia.
                O daughter of Babylon, thou wretched one, blessed shall he be who shall reward thee Wherewith thou hast rewarded us. Alleluia.
                Blessed shall he be who shall seize and dash thine infants against the rock. Alleluia (Thrice)
            """
            ,'after50': """
                In Tone VIII:
                Glory ..., The gates of repentance, do Thou open unto me, O Giver of Life, * for early in the morning my spirit seeketh Thy holy temple, * bearing the temple of my body all defiled. * But as One who art compassionate * cleanse it by Thy loving-kindness and mercy. Now & ever ..., Guide me on the paths of salvation, O Theotokos: * for I have polluted my soul with shameful deeds * and wasted all my life in slothfulness. * but by thine intercessions * do thou deliver me from all impurity.
                In Tone VI:
                Have mercy upon me, O God, * according to Thy great mercy: * and according to the multitude of Thy compassion * blot out my transgressions.
                In Tone VIII:
                As I the wretched one ponder the multitude of evil deeds I have done, * I tremble for fear of the dread day of judgment. * But trusting in Thy compassionate mercy, * like David do I cry unto Thee: * "Have mercy upon me, O God, according to Thy great mercy".
            """
            ,'canon': """
                ODE I
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Taking up the Song of Moses, ...
                Refrain: Have mercy on me, O God, have mercy on me.
                O Jesus my God, as the Prodigal Son accept me now in repentance, for I
                have lived all my life in slothfulness and provoked Thee to anger.
                Refrain: Have mercy on me, O God, have mercy on me.
                The divine gifts which Thou didst once give me, I have sinfully wasted. I
                have departed far from Thee and lived Prodigally. O compassionate Father,
                accept me also who doth return.
                Glory ..., Open Thy fatherly embrace now and accept me also as the
                Prodigal Son O most merciful One, that I may glorify Thee with thanksgiving.
                Now & Ever ..., Bestow upon me O God, the fullness of Thy goodness, and
                look not upon the multitude of my offenses, but by the holy prayers of Thy
                Mother be Thou my Benefactor.
                Katavasia in Tone II: Taking up the Song of Moses, * cry aloud O my
                soul: * “A helper and protector for me unto salvation. * hath my God
                become, * and I glorify Him”.
                ODE III
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: My mind hath not brought forth good fruit, ...
                Refrain: Have mercy on me, O God, have mercy on me.
                Utterly beside myself, I have clung insanely to the sins suggested to me by
                the passions. But do Thou accept me, O Christ, as the Prodigal.
                Refrain: Have mercy on me, O God, have mercy on me.
                With the voice of the Prodigal I cry aloud: I have sinned, O Father; and like
                him, receive me now in Thine embrace and reject me not.
                Glory ..., Open Thine arms, O Christ, and mercifully receive me as I return
                from the distant land of sin and the passions.
                Now & Ever ..., O fair among women, enrich me with the vision of good
                things, I who have brought myself to poverty by my many sins, O pure One, that
                I may glorify thee.
                Katavasia: My mind hath not brought forth good fruit, * but do Thou
                show me to be fruitful * in Thy compassion O God, * Thou husbandman
                of all good things.
                Sessional Hymns from the Triodion, in Tone I:
                Make haste to open unto me Thy fatherly embrace, * for I have wasted my
                life in prodigal living. * In the unfailing wealth of Thy compassion, O Savior, *
                turn not away from my heart in its poverty, * for with compunction I cry unto
                Thee, O Lord: ** “O Father, I have sinned against heaven and before Thee”.
                Glory ..., Now & ever ..., in Tone I:
                O pure Theotokos Virgin * who hast not known a man, * thou alone art the
                guardian and protection of the faithful: * deliver from danger and affliction, and
                every evil circumstance * all who put their trust in thee, O Maiden, ** and save
                our souls by thy divine intercessions.
                ODE IV
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: The prophet foreseeing Thy birth from a virgin, ...
                Refrain: Have mercy on me, O God, have mercy on me.
                The wealth of blessings which Thou gavest me, O heavenly Father, I have
                wickedly wasted and become a slave of foreign strangers. Wherefore I cry to
                Thee: I have sinned against Thee; receive me as of old Thou didst receive the
                Prodigal, and open Thine arms to me.
                Refrain: Have mercy on me, O God, have mercy on me.
                I have become enslaved to every evil and in my wretchedness I have bowed
                down before those who provoke the passions; through heedlessness I care not
                for my well-being, have compassion on me O Savior, heavenly Father, for I flee
                for refuge to Thine abundant compassions.
                Glory ..., I am filled with every shameful thing and dare not look up at the
                height of heaven, for I have bowed down to sin. But now I return and cry with
                compunction: I have sinned against Thee; receive me, O King of all.
                Now & Ever ..., Thou art the help of all mankind, the sure hope of all
                Christians, thou refuge O pure one of the saved. Save me by thy maternal
                intercessions and deem me worthy of the life to come.
                Katavasia: The prophet foreseeing Thy birth from a virgin, * prophesied
                crying aloud: * “I have heard report of Thee, and I was afraid; * For from
                the South, from the Overshadowed mountain * shalt thou come forth O
                Christ”.
                ODE V
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: The night is far spent, the day is at hand ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I have been enslaved to foreign strangers, exiled in the land of corruption,
                and I am filled with shame. But returning now, O merciful One, I cry to Thee: “I
                have sinned”.
                Refrain: Have mercy on me, O God, have mercy on me.
                O heavenly Father, in Thy fatherly compassion accept me now, returning
                from wickedness, and reject me not in Thine exceedingly great mercy.
                Glory ..., I am incapable of looking up to the height of heaven, having
                angered Thee beyond measure, O Christ, but knowing Thy merciful compassion,
                I cry: I have sinned against Thee, be Thou merciful to me and save me.
                Now & Ever ..., O all-holy Virgin, full of grace, thou who didst bear the
                redeemer of all, by thy prayers lighten the heavy burden of my sins.
                Katavasia: The night is far spent, the day is at hand: * Thy light hath
                shone upon the world! * Therefore the ranks of angels sing Thy praises, *
                and all things glorify Thee, O Lord!
                ODE VI
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: I am held fast in the depths of sin ...
                Refrain: Have mercy on me, O God, have mercy on me.
                The depth of sin doth now hold me fast, and the tempest of transgressions
                doth overwhelm me. Guide me to the safe haven of life, O Christ my God, and
                save me, O King of glory.
                Refrain: Have mercy on me, O God, have mercy on me.
                I have wasted in riotous living the riches which the Father hath given me,
                and am now filled with shame and enslaved to fruitless thoughts. Wherefore I cry
                unto Thee: “O Lover of mankind be compassionate unto me and save me”.
                Glory ..., In hunger I find myself deprived of every blessing, and exiled from
                Thee O all-good one, be compassionate to me who now return unto The, and
                save me O Christ, who doth praise Thy love for mankind.
                Now & Ever ..., O Maiden who didst conceive Christ the Savior and Master,
                make me, who in poverty lacketh all that is good, worthy of salvation, O pure
                one, that I may praise thy majesty.
                Katavasia: Held fast in the depths of sin O Savior, * I am overwhelmed by
                the sea of life, * but as Jonah was delivered from the sea-monster, * so also
                deliver me from the passions, * and save me.
                Kontakion from the Triodion, in Tone III:
                Foolishly have I fled from Thy glory, O Father, * in wickedness wasting the
                wealth that Thou hast given me. * Wherefore with the voice of the Prodigal I cry
                unto Thee: * “I have sinned before Thee, O compassionate Father. ** Accept me
                who repent, and make me as one of Thy hired servants”.
                Ikos: Every day our Savior doth teach us with His own voice: let us
                therefore hearken to the Scriptures concerning the Prodigal who once again
                became wise, and with faith let us emulate the good example of his repentance.
                With humbleness of heart let us cry out to Him Who knoweth the hidden things
                of all: “We have sinned against Thee, O compassionate Father, and can never be
                worthy to be called Thy children as we were before. But since Thou art by nature
                the Lover of mankind, accept me and make me as one of Thy hired servants”.
                SYNAXARION READING
                Verse: If anyone be a prodigal as I, take courage and turn back;
                Verse: For the gates of God’s mercies are opened to all.
                On this day we celebrate the Sunday of the Prodigal Son, dedicated as the
                second service of the Triodion by the divine Fathers for the following reason.
                There are some who recognize much in themselves that is unbecoming, who live
                a life of great dissipation from their youth, whose lives are full of drunkenness
                and immorality, who having fallen thus into the depths of evil, become
                despondent, giving birth to pride, from whence they have no desire to advance
                to any of the virtues, preferring their bondage to evil and falling ever deeper into
                evil. Having a fatherly love for even these individuals, and desiring to lead them
                out of their despair, the Holy Fathers prescribed this parable for the second
                preparatory Sunday in order to tear up the passion of despair by the roots, to
                lead them to acceptance of the virtues, and to demonstrate to sinners the
                abundance of God’s compassion upon sinners and prodigals in His great
                goodness and love for mankind. For there is no sin which cannot be overcome
                by the knowledge of His love for mankind, and this is what is presented in this
                parable of Christ. Now the sons of man, that is of the Word, God and Man, are
                two: the righteous and the sinful. It is the eldest who abides ever in God’s
                blessings, following His commandments and remaining always by Him. But the
                younger son, having become attached to sin and renouncing his closeness to
                God through shameful deeds, has wasted God’s love for mankind and for him
                and has lived as a prodigal. For having completely rejected Him after whose
                image he was created, and having followed an evil demon, willingly enslaving
                himself to this demon’s pleasure, he was unable to fulfill his desire. For sin is an
                unsatisfying thing that becomes an habitual source of temporary pleasure. It may
                be compared to the husks that are fed to swine. At first it seems that they might
                be something tasty, but they turn out to be very dry and are much like weeds,
                which is how sin takes possession. For the Prodigal Son had hardly come to his
                senses when, perishing from hunger for virtue, he comes to his father, saying,
                “Father, I have sinned before heaven and before thee, and I am not worthy to be
                called thy son.” Yet the father receives him in repentance, not reproaching him,
                but embracing him and kissing him in a display of divine and fatherly love. And
                he clothes him, a symbol of baptism, putting a ring on his finger, a symbol of the
                grace of the most holy Spirit. He also puts sandals on his feet, not so much as a
                protection from some serpent or scorpion that might sting him on his path to
                God, but rather as a means of crushing the heads of those creatures. And then in
                a tremendous display of joy he slaughters the fatted calf for him, his onlybegotten Son, and the Father grants him communion of his body and blood.
                Now the elder son expresses his amazement at his father’s limitless mercy. But
                the lover of mankind exhorts him to silence with loving and kind words of
                humility, saying, “Thou art ever with me, and it was meet that we should make
                merry and be glad, for my son was formerly dead in his sin and is alive again,
                having repented of the foolish things he has done. He was lost, since he was far
                from me in his licentious habits, and he was found by me, suffering in my
                compassion and calling him back in my mercy.” This parable may be applied to
                us as well, which is why the holy Fathers have prescribed it for today. We who
                have sinned as the prodigal are encouraged to weed out despair and fear through
                repentance, confession and good deeds. For this is a great aid and a powerful
                weapon against the assaults of the adversary.
                In Thine ineffable love for mankind, O Christ our God,
                have mercy upon us. Amen.
                ODE VII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Like unto the Cherubim, the Children rejoicing ...
                Refrain: Have mercy on me, O God, have mercy on me.
                I have bowed down miserably to the pleasures of the flesh and have become
                wholly enslaved to those who incite the passions; and I have become a stranger
                to Thee O Lover of mankind. But now I cry with the voice of the Prodigal: “I
                have sinned, O Christ, despise me not, for Thou alone art merciful”.
                Refrain: Have mercy on me, O God, have mercy on me.
                I call out, “I have sinned,” and I dare not look up at the height of heaven, O
                King of all; for foolishly I alone have angered Thee, turning away from Thy
                commandments. Wherefore, since Thou alone art good, cast me not away from
                Thy presence.
                Glory ..., By the prayers of the apostles, the prophets, the saints, the holy
                martyrs and the righteous, forgive me all the transgressions, by which I have
                angered Thy compassionate goodness, that I may hymn Thee throughout all
                ages.
                Now & Ever ..., O Theotokos, thou art more glorious than the cherubim
                and seraphim and all the heavenly hosts. With them, O all-immaculate one,
                entreat Him Who took flesh from thee, the divine Word of the beginningless
                Father, that we all may be found worthy of eternal blessings.
                Katavasia: Like unto the Cherubim, the Children rejoicing in the furnace
                sang: * “Blessed art Thou O God, * for in truth Thou hast brought this
                judgment upon us * because of our sins, * Thou art supremely praised
                and glorified throughout all ages”.
                ODE VIII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Unto Him Who of old prefigured the miracle ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                O Thou Who didst come down to earth to save the world through Thy
                voluntary self-emptying and Who, for the sake of Thy great compassion, hath
                redeemed me who am lacking in all good works, since Thou art merciful, save
                me.
                Refrain: Have mercy on me, O God, have mercy on me.
                I have departed far from Thy commandments and, wretch that I am, have
                wholly enslaved myself to the deceiver. But having now turned back, as did the
                Prodigal of old, accept me as I fall down before Thee, O heavenly Father.
                Refrain: Let us bless the Father, Son, and Holy Spirit, the Lord!
                Ruled by corrupting thoughts, I am full of darkness and separated far from
                Thee, and have lost all care for myself, O compassionate One. Therefore save
                me as I fall down before Thee in repentance.
                Now & Ever ..., O pure Birthgiver of God, the only restoration of the fallen,
                raise me up who am wholly crushed and humbled by every kind of sin.
                Verse: We praise, bless and worship the Lord, chanting and supremely
                exalting Him throughout all ages.
                Katavasia: Unto Him Who of old prefigured the miracle of the Virgin, *
                unto Moses in the burning-bush * on Mount Sinai, * let us sing, bless and
                supremely exult throughout all ages.
                And then we chant the Hymn of the Most Holy Theotokos (the Magnificat)
                ODE IX
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Who born on Earth hath ever heard of, or beheld ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                Behold, O Christ, the affliction of my heart; behold my turning back; behold
                my tears, O Savior, and despise me not. But for the sake of Thy compassion
                embrace me also once again, that, with the multitude of the saved, I may with
                thanksgiving sing the praises of Thy mercy.
                Refrain: Have mercy on me, O God, have mercy on me.
                Like the thief I cry to Thee, “Remember me.” and like the Publican, with
                eyes cast down to earth, I beat my breast saying, “Be merciful.” Like the Prodigal
                O compassionate One, deliver me from every evil, O King of all, that I may sing
                the praises of Thy boundless compassion.
                Refrain: Have mercy on me, O God, have mercy on me.
                Groan now, O my wretched soul, and cry aloud to Christ: “O Lord Who for
                my sake didst voluntarily become poor, in my poverty I lack every good work: do
                Thou enrich me with the abundance of Thy blessings, for Thou alone good and
                plenteous in mercy”.
                Glory ..., As Thou, O Good One, once rejoiced at the voluntary return of
                the Prodigal: do Thou also rejoice over me, wretched as I am, and open to me
                Thine honorable embrace, that saved I may sing the praises of Thy boundless
                compassion.
                Now & Ever ..., By thy light-giving intercessions, I pray thee O Virgin,
                enlighten the eyes of my mind darkened by evil and lead me into the paths of
                repentance, that I may rightly sing thy praises: for thou hast inexpressibly given
                birth to the Word in the flesh.
                Katavasia: Who born on Earth hath ever heard of, or beheld, * a Virgin
                miraculously conceiving in her womb, * and painlessly giving birth to a
                child, * wherefore we magnify thee O pure Virgin.
            """
            ,'exapostilarion': 'Glory ..., in Tone III: \nI have wasted, and in my wretchedness * spent, all the riches which Thou hast given me O Savior, * and having lived prodigally, I have been deceived by the demons. * Wherefore, turn me back, * and accept me as the Prodigal, ** O compassionate Father, and save me. \nNow & ever ..., Theotokion:\nO holy Mother and Virgin, * thou great boast of the apostles, martyrs, prophets and venerable saints, * gain the gracious favor of thy Son and Lord towards us thy servants * O Birthgiver of God, * when He shall sit to judge each and every one ** according to their own legacy.'
            ,'aposticha': '5 Resurrection Stichera, in the Tone of the week: \nThen, 3 Stichera from the Triodion, in Tone II: \nVerse: Praise Him with tuneful cymbals, praise Him with cymbals of jubilation. * Let every breath praise the Lord. I bring to Thee, O Lord, * the cry of the Prodigal: * “I have sinned in Thy sight, O good One; * I have wasted the riches of Thy gifts. ** But receive me who repent, O Savior, and save me. \nVerse: Arise, O Lord my God, let Thy hands be lifted high; * forget not Thy paupers to the end. \nIn Tone IV: Like the Prodigal Son * I come to Thee, O compassionate One. * I have wasted my whole life in exile; * I have scattered the wealth which Thou hast given me, O Father. * Receive me who repent, O God, ** and have mercy on me. \nVerse: I will confess Thee, O Lord, with my whole heart, * I will tell of all Thy wonders. \nIn Tone VIII: Having lived prodigally, I have wasted the riches which the Father hath given me; * having spent them all I am now destitute, * and dwell in the land of the wicked. * I can no longer bear to live among them, * but turning back I cry unto Thee: * “O merciful Father, I have sinned against heaven and before Thee, * and I am no more worthy to be called Thy son: ** make me as one of Thy hired servants, O God, and have mercy on me”.'
            ,'aposticha_theotokion': 'Glory ..., in Tone VI: \nO Good One, I have departed far from Thee, * but forsake me not, neither reject me from Thy Kingdom. * The evil enemy hath stripped me and taken all of my wealth; * I have squandered, like the Prodigal, the good gifts given to my soul. * But now I have arisen and returned, and to Thee I cry aloud: * “Make me as one of Thy hired servants. * For, for my sake on the Cross Thou didst stretch out Thy sinless hands, * to snatch me from the evil beast * and to clothe me once again in my first raiment ** for Thou alone art plenteous in mercy. \nNow & ever ..., Theotokion, in Tone II: \nMost Blessed art Thou, O Virgin Theotokos, * for through Him Who became incarnate of thee is Hades led captive, * Adam recalled, the curse annulled, Eve set free, death slain, * and we are given life. Wherefore, we cry aloud in praise: * Blessed art Thou, O Christ God, * Who hast been thus wellpleased, glory to Thee.'
        } #Matins
        ,'liturgy': {
            'beatitudes': [
                'The depth of sin doth now hold me fast, and the tempest of transgressions doth overwhelm me. Guide me to the safe haven of life, O Christ my God, and save me, O King of glory.'
                ,'I have wasted in riotous living the riches which the Father hath given me, and am now filled with shame and enslaved to fruitless thoughts. Wherefore I cry unto Thee: “O Lover of mankind be compassionate unto me and save me”.'
                ,'Glory ..., In hunger I find myself deprived of every blessing, and exiled from Thee O all-good one, be compassionate to me who now return unto The, and save me O Christ, who doth praise Thy love for mankind.'
                ,'Now & Ever ..., O Maiden who didst conceive Christ the Savior and Master, make me, who in poverty lacketh all that is good, worthy of salvation, O pure one, that I may praise thy majesty.'
            ]
            ,'kontakion': 'In Tone III.\n Foolishly have I run away from Thy glory, O Father, * wasting in sin the wealth that Thou gavest me. * Wherefore with the words of the Prodigal I cry unto Thee: * I have sinned before Thee, compassionate Father. ** Accept me in repentance and make me as one of Thy hired servants.'
            ,'readings': """
                1ST EPISTLE TO THE CORINTHIANS: (I COR 6:12-20)
                Brethren: All things are lawful unto me, but all things are not expedient: all
                things are lawful for me, but I will not be brought under the power of any. Meats
                for the belly, and the belly for meats: but God shall destroy both it and them.
                Now the body is not for fornication, but for the Lord; and the Lord for the
                body. And God hath both raised up the Lord, and will also raise up us by his
                own power. Know ye not that your bodies are the members of Christ? shall I
                then take the members of Christ, and make them the members of an harlot? God
                forbid. What? know ye not that he which is joined to an harlot is one body? for
                two, saith he, shall be one flesh. But he that is joined unto the Lord is one spirit.
                Flee fornication. Every sin that a man doeth is without the body; but he that
                committeth fornication sinneth against his own body. What? know ye not that
                your body is the temple of the Holy Ghost which is in you, which ye have of
                God, and ye are not your own? For ye are bought with a price: therefore glorify
                God in your body, and in your spirit, which are God’s.

                GOSPEL ACCORDING TO ST. LUKE (15:11-32)
                The Lord spake a parable saying: A certain man had two sons: And the
                younger of them said to his father, Father, give me the portion of goods that
                falleth to me. And he divided unto them his living. And not many days after the
                younger son gathered all together, and took his journey into a far country, and
                there wasted his substance with riotous living. And when he had spent all, there
                arose a mighty famine in that land; and he began to be in want. And he went and
                joined himself to a citizen of that country; and he sent him into his fields to feed
                swine. And he would fain have filled his belly with the husks that the swine did
                eat: and no man gave unto him. And when he came to himself, he said, How
                many hired servants of my father’s have bread enough and to spare, and I perish
                with hunger! I will arise and go to my father, and will say unto him, Father, I
                have sinned against heaven, and before thee, And am no more worthy to be
                called thy son: make me as one of thy hired servants. And he arose, and came to
                his father. But when he was yet a great way off, his father saw him, and had
                compassion, and ran, and fell on his neck, and kissed him. And the son said unto
                him, Father, I have sinned against heaven, and in thy sight, and am no more
                worthy to be called thy son. But the father said to his servants, Bring forth the
                best robe, and put it on him; and put a ring on his hand, and shoes on his feet:
                And bring hither the fatted calf, and kill it; and let us eat, and be merry: For this
                my son was dead, and is alive again; he was lost, and is found. And they began to
                be merry. Now his elder son was in the field: and as he came and drew nigh to
                the house, he heard musick and dancing. And he called one of the servants, and
                asked what these things meant. And he said unto him, Thy brother is come; and
                thy father hath killed the fatted calf, because he hath received him safe and
                sound. And he was angry, and would not go in: therefore came his father out,
                and intreated him. And he answering said to his father, Lo, these many years do I
                serve thee, neither transgressed I at any time thy commandment: and yet thou
                never gavest me a kid, that I might make merry with my friends: But as soon as
                this thy son was come, which hath devoured thy living with harlots, thou hast
                killed for him the fatted calf. And he said unto him, Son, thou art ever with me,
                and all that I have is thine. It was meet that we should make merry, and be glad:
                for this thy brother was dead, and is alive again; and was lost, and is found.
            """
        } #Liturgy
    } #Service
    ,'-57': { #Meatfare Saturday
        'vespers': {
            'stichera_tone': 'In Tone VIII:'
            ,'stichera': [
                """
                    Calling to remembrance by name today * all the dead from all the ages *
                    who with faith have lived piously. * O ye faithful, let us sing praises to the
                    Savior and Lord, * asking Him fervently to grant them a good defense * in the
                    hour of judgment before our God, * who will judge all the earth. * May they
                    receive a place at His right hand in joy; * may they dwell in glory with the
                    righteous and the saints, ** and be deemed worthy of His heavenly Kingdom.
                """
                ,"""
                    By Thine own Blood, O Savior, * Thou hast ransomed mankind, * and by
                    Thy death Thou hast delivered us from bitter death, * granting us life eternal by
                    Thy Resurrection. * Grant rest then, O Lord, to all those who have fallen asleep
                    in godliness, * whether in the wilderness or in the city, * on the sea or on land, *
                    in every place, sovereigns, rulers and hierarchs, * priests, monastics and those
                    married, of every age and every race, ** and deem them worthy of Thy heavenly
                    Kingdom.
                """
                ,"""
                    By Thine arising from the dead, O Christ, * no longer doth death rule over
                    those that have died in piety. * Wherefore we pray fervently: * Grant rest in Thy
                    courts and in the bosom of Abraham * to Thy servants from Adam to this
                    present day * who have worshiped Thee in purity, * our fathers and brethren,
                    friends and kin, * all who in this life have offered faithful service to Thee, * and
                    who have now departed to be with Thee, ** O God, and deem them worthy of
                    Thy heavenly Kingdom.
                """
            ]
            ,'doxastichon': """
                I lament, and weep when I see death * and look upon our beauty, formed
                according to God’s image, * lying in the grave disfigured, inglorious, and bereft
                of animate form. * O strange wonder! What mystery is this concerning us? *
                How have we been delivered unto corruption? * How have we been yoked to
                death? * All this, as is written, is by the command of God, ** who granteth rest
                unto the departed.
            """
            ,'prokeimenon':"""
                Prokeimenon in Tone VIII:
                Verse: Blessed are they whom Thou hast chosen and taken to Thyself, O
                Lord. (Alleluia x3)
                Verse: Their memorial is unto generation and generation. (Alleluia x3)
                Verse: Their souls shall dwell among good things. (Alleluia x3)
            """
            ,'aposticha_theotokion': """
                Glory ..., in Tone VI:
                My beginning and foundation * was accomplished by Thy creative will, * for
                Thou didst will to fashion me * as a living creature from visible and invisible
                natures; * having brought forth my body from the earth, * and given me a soul
                by Thy divine and quickening breath. * Wherefore, O Savior, * grant rest unto
                Thy servants in the land of the living, ** in the tabernacles of the righteous.
                Now & ever ..., Theotokion, in Tone VI:
                By the prayers of her that gaveth birth to Thee O Christ, * and of Thy
                martyrs and apostles, * the prophets and holy hierarchs, * the venerable, the
                righteous and of all the saints, ** grant rest to Thy departed servants.
            """
            ,'apolytichia':"""
                The Troparion, in Tone VIII:
                O Thou Who by the depth of Thy wisdom * dost provide all things out of
                love for man, * and grantest unto all that which is profitable, O only Creator: *
                Grant rest, O Lord, to the souls of Thy servants; ** for in Thee have they
                placed their hope, O our Creator and Fashioner and God.
                Glory ..., Now & ever ..., Theotokion, in Tone VIII:
                In thee do we have a rampart and calm haven * and an intercessor
                acceptable to God, ** Whom thou didst bear, O Theotokos unwedded, thou
                salvation of the faithful.
            """
        } #Vespers
        ,'matins': {
            'troparion': """
                Troparion of the day, in Tone VIII;
                O Thou Who by the depth of Thy wisdom * dost provide all things out of
                love for man, * and grantest unto all that which is profitable, O only Creator: *
                Grant rest, O Lord, to the souls of Thy servants; ** for in Thee have they
                placed their hope, O our Creator and Fashioner and God.
                Glory ..., Now & ever ..., Theotokion:
                In thee do we have a rampart and calm haven * and an intercessor
                acceptable to God, ** Whom thou didst bear, O Theotokos unwedded, thou
                salvation of the faithful.
            """
            ,'evlogitaria':"""
                The Evlogitaria of the Dead, in Tone V:
                Refrain: Blessed art Thou, O Lord; teach me Thy statutes.
                The Choir of the Saints hath found the Fountain of Life * and the Door of
                Paradise. * May I also find the way through repentance. * I am the lost sheep,
                call me, O Savior, and save me.
                Refrain: Blessed art Thou, O Lord; teach me Thy statutes.
                Ye that have preached the Lamb of God, * and like lambs were slain, O holy
                ones, * translated unto life that ageth not and is everlasting, * fervently entreat
                Him, O ye martyrs, * to grant us forgiveness of our sins
                Refrain: Blessed art Thou, O Lord; teach me Thy statutes.
                Ye that have trod the narrow way of sorrow; * all ye that in life have taken
                up the Cross as a yoke, * and have followed Me in faith, * come, enjoy the
                honors and heavenly crowns * which I have prepared for you.
                Refrain: Blessed art Thou, O Lord; teach me Thy statutes.
                I am an image of Thine ineffable glory, * though I bear the wounds of sin; *
                take compassion on Thy creature, O Master, * and cleanse me by Thy lovingkindness; * and grant me the longed-for fatherland, * making me again a citizen
                of paradise.
                Refrain: Blessed art Thou, O Lord; teach me Thy statutes.
                O Thou Who of old didst fashion me out of nothing, * and didst honor me
                with Thine image divine, * but because of my transgression of Thy
                commandment * didst return me again unto the earth, from which I was taken:
                * Restore to me again Thy likeness, ** that I may be refashioned in that former
                beauty.
                Refrain: Blessed art Thou, O Lord; teach me Thy statutes.
                Grant rest, O God, to the souls of Thy servants, * and commit them to
                paradise, * where the choirs of the Saints O Lord, * and of the righteous shine
                as luminaries; * Grant rest, unto Thy departed servants, * overlooking all their
                transgressions.
                Glory ..., in Tone V:
                The triple radiance of the one Godhead * let us piously hymn, crying aloud:
                * Holy art Thou, O beginningless Father, * co-beginningless Son, and Divine
                Spirit; * Do Thou enlighten us Who with faith Worship Thee ** and snatch us
                from the eternal fire.
                Now & ever ..., Theotokion, in Tone V:
                Rejoice, O thou pure one, Who hast given birth to God in the flesh * for
                the salvation of all, * and through Whom mankind hath found salvation; *
                through thee may We find paradise, ** O Theotokos, pure and blessed.
            """
            ,'canon': """
                The Canons
                We chant the Canon of the patron saint of the church or monastery
                With 6 Troparia (including the Irmos), and the Canon for the reposed
                from the Triodion, with 8 Troparia.
                ODE I, in Tone VIII:
                Canon of the temple, then:
                Irmos: Let us, O people, send up a melody . . . .
                Refrain: Wondrous is God in His saints, the God of Israel.
                As we celebrate today the memory of the dead from the ages, let us all
                entreat Christ to deliver from the everlasting fire those who have fallen asleep in
                the faith, and in the hope of eternal life.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                In the depths of Thy judgments, O Christ, with fullness of wisdom Thou
                hast preordained the end of each man’s life, its appointed time and manner.
                Therefore, All-Merciful One, at the judgment save those in every land whom
                the grave hath hidden.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                It is Thee who hath limited the time of our life here; therefore, when we
                waken from the night of life, make us sons of the never-ending day: Orthodox
                priests and kings and all Thy faithful people.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those hidden by the waters, or fallen in battle, swallowed by earthquake,
                murdered by murderers, or consumed by fire, the faithful, and grant them, O
                merciful One, a place with the righteous.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                Overlook all the transgressions of the flesh, O our Savior, in every age, by
                every nation of mankind, and grant that all who must give answer to Thee may
                stand before the judgment-seat of Thee the Creator, uncondemned.
                Glory ..., I sing the praises of Three self-dependent Hypostases in One
                Nature, the Father unbegotten, the Son begotten, and the Holy Spirit:
                sovereignty and power without beginning, a single Godhead.
                Now & ever ..., Theotokion: Truly thou dost appear as heaven on earth, far
                greater than the highest heavens, O unwedded Virgin. For from thee hath
                shone forth upon the world the Sun and King of righteousness.
                Katavasia: Let us, O ye people, send up a hymn * unto our wondrous
                God * Who hath freed Israel from bondage, * chanting a hymn of victory
                * and crying aloud: * We sing unto Thee, O only Master.
                ODE II
                (Note: The Canon for the Patron does not have an ODE II, therefore this
                Irmos is chanted in place of the Irmos of the Canon of the temple.)
                Irmos: See now, see that I am your God, * begotten of the Father before
                all ages, * conceived without a man in these latter times from the Virgin,
                * abolishing the sin of the forefather Adam, * as the Lover of mankind.
                Refrain: Wondrous is God in His saints, the God of Israel.
                See now, see that I am your God, who in righteous judgment hath fixed the
                bounds of life, bringing forth from corruption into incorruption all who have
                fallen asleep in the hope of the eternal resurrection.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                O Lord, Thou receivest from the four corners of the earth those who have
                died in faith, at sea and on the land, in rivers, springs, lakes or wells, devoured
                by wild beasts, birds or creeping things. Grant rest to them all.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                O Lord, all that is, is in the palm of Thy hand, Thou dost discern all things
                a-priori, before they dissolve into the four elements: in Thy coming do Thou
                restore and raise up all, forgiving them all their offences committed in
                knowledge or in ignorance.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                O Lord, how fearful shall be Thy second coming! For as lightning Thou
                shalt come on earth and raise up all Thy creatures to be judged. Grant to those
                who lived with faith in Thee, to meet Thee on that day and be counted worthy
                to dwell with Thee.
                Glory ..., A most perfect unity in Three Hypostasis, a supreme Godhead, O
                Father unbegotten, Son only-begotten, Spirit proceeding from the Father and
                made manifest through the Son: single in essence and in nature, One Lordship
                and One Kingdom, save us all.
                Now & ever ..., Theotokion: The wonder of thy conceiving is beyond
                speech, O Mother and Virgin: for how didst thou give birth and yet remain
                undefiled? How dost thou bear a child, without knowing a man? This news is
                new and wonderful to me, how, surpassing nature, the Word of God was born
                of thee.
                Katavasia: See now, see that I am your God, * begotten of the Father
                before all ages, * conceived without a man in these latter times from the
                Virgin, * abolishing the sin of the forefather Adam, * as the Lover of
                mankind.
                ODE III
                Canon of the temple, then:
                Irmos: O Word of God who hast made firm. . .
                Refrain: Wondrous is God in His saints, the God of Israel.
                To those who have passed through the course of this life in the glory of
                piousness, do Thou O God, make worthy to be adorned with a crown of
                righteousness, and may they enjoy eternal blessings.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those who have been suddenly snatched away, burnt by lightning, frozen
                by cold, or struck down by any other calamity, grant rest, O God, when Thou
                shalt try all things by fire.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those who have sailed across the ever-troubled sea of this life, grant safe
                anchorage O Christ, in the harbor of immortal life with Thee, nurtured by an
                Orthodox life.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                Those whom the creatures of the sea or the birds of the air have devoured,
                by Thy judgments O Christ God, raise up in glory on the Last Day.
                Glory ..., In my thoughts I distinguish Three Hypostases within the
                simplicity of the divine Oneness, without commingling their characteristics, for,
                like the swift flash of lightning, the Three-fold radiance is seen in a Unity.
                Now & ever ..., Theotokion: Mind cannot fathom the wonder brought to
                pass in thee. For thou didst conceive without a man, O pure One, and hast
                given birth while keeping thy virginity. Wherefore the angelic hosts and the race
                of mankind sing thy praises throughout the ages.
                Katavasia: O Word of God who hast made firm the heavens * with Thine
                own hand, * through the enlightenment of Thy true knowledge * make
                firm our hearts, * for we have put our trust in Thee.
                The usual Small Litany after the third Ode.
                Sessional Hymn, in Tone V:
                O Savior, who for our sakes didst endure the Cross and death, * who didst
                put Hades to death and raised the dead, * grant rest, O Lover of mankind, * to
                those who have departed from us; * and at Thy dread and fearful Coming, O
                Giver of Life, * in the multitude of Thy mercies * deem them worthy of Thy
                Kingdom.
                Glory ..., the foregoing is repeated.
                Now & ever ..., Theotokion: Show forth thy ready protection, help and
                mercy * upon thy servants, O pure one; * dampen the waves of vain thoughts, *
                and raise up my fallen soul, O Theotokos, * for I know, O Virgin, I know, **
                that thou canst do whatsoever thou dost will.
                ODE IV
                Canon of the temple, then:
                Irmos: From the overshadowed mountain. . . .
                Refrain: Wondrous is God in His saints, the God of Israel.
                Fathers and forefathers, grandfathers and great-grandfathers, from the first
                times up to these last times, who have died in holiness of life and in proper
                faith: remember them all, O our Savior.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those who died on mountains, or on the road, living in desert places,
                passing away in the faith, monks and the married, young and old; grant unto
                them all, O Christ, to dwell with the saints.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those who with faith were suddenly taken from this life inopportunely,
                in the midst of joy or sorrow, of prosperity or misfortune: grant rest, our Savior,
                to them all.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those killed by the sword, by falling from their horse, overwhelmed by
                hall, snow or storms, crushed by stones or suffocated in the earth, grant rest, O
                Christ our Savior.
                Glory ..., Strange it is that the Godhead should be one and three, fully
                present in each single Person without division: for the Father, Son and Holy
                Spirit are worshipped as one God.
                Now & ever ..., Theotokion: Guide us O Virgin, by thine intercessions, for
                we are buffeted by the stormy waves of sin: and lead us to the safe-haven of
                salvation, delivering us from every danger.
                Katavasia: From the overshadowed mountain, * from the only
                Theotokos, * the Prophet in divine vision * foresaw Thy coming in the
                flesh, O Word, * and with fear he glorified Thy power.
                ODE V
                Canon of the temple, then:
                Irmos: O God my spirit seeketh Thee early ...
                Refrain: Wondrous is God in His saints, the God of Israel.
                Celebrating today, O Lord, the memorial of all who from the ages have died
                in the true faith, we fervently cry to Thee: Grant them rest with all Thy saints.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                Those whom Thou hast taken from every generation, Orthodox kings,
                rulers and monks, do Thou O compassionate One, deliver from eternal
                torment.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                Thou knowest what is best for all the creatures Thou hast formed: To those
                whom Thou hast permitted to die unexpectedly, by some sudden mishap do
                Thou deliver from every torment, O God.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                From the ever-burning fire, from the darkness without light, from the
                gnashing of teeth and the worm that torments without ceasing, from every
                torment deliver, O our Savior, all who have died in faith.
                Glory ..., One in throne, without beginning, threefold Hypostatic Unity,
                single in Nature yet distinct in Hypostases, unite us in the one will of Thy
                commandments.
                Now & ever ..., Theotokion: Thou art higher in honor than the fiery
                seraphim, O pure One, for thou hast borne the Him Who is fearful to
                approach, the Savior, Who by taking flesh from thee hath rendered our earthly
                nature godlike.
                Katavasia: O God my spirit seeketh Thee early at dawn, * for the light of
                Thy commandments precede Thy coming: * with them illumine our
                minds, O Master, * and guide us on the path of life.
                ODE VI
                Canon of the temple, then:
                Irmos: Held fast by a multitude of sins ...
                Refrain: Wondrous is God in His saints, the God of Israel.
                Thou hast loosed the pains of death, having suffered <the Passion>, O our
                God, Thou author of Life: grant rest to Thy servants who have fallen asleep
                from the ages.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those whom, according to Thine inscrutable judgments, Thou hast
                permitted to be slain by drugs or by poison, or through choking on bones, grant
                rest, O Lord, with Thy saints.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                When Thou shalt come as judge and all things stand naked before Thy face,
                then in Thy mercy spare, O God, those who served Thee faithfully.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                When Thine Archangel shall sound the last trumpet, awakening all to the
                resurrection of life, then, O Christ, grant rest to Thy servants.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                O God, count all whom Thou hast taken from the ages, the faithful from
                every nation of mankind, worthy to glorify Thee with Thy servants forever.
                Glory ..., Thrice-holy Godhead, One in throne, Father, Son and Spirit, Thou
                art my God, holding all in unity by Thine almighty Power.
                Now & ever ..., Theotokion: Leap for joy, O Jesse the forefather; for from
                thy root hath Sprung forth the Flower of Life that saveth the world, Christ God
                born from the pure Maiden.
                Katavasia: Held fast by a multitude of sins O Lover of mankind, * like
                the Prophet I fall down before Thy tender compassions. * Accept me O
                Lord and save me.
                The Small Litany for the Reposed, then:
                Kontakion in Tone VIII;
                With the Saints grant rest, O Christ, * to the souls of Thy servants, * where
                there is neither * pain, nor sorrow, nor sighing, * but life everlasting.
                Ikos: Thou alone art immortal, * Who hast created and fashioned man; *
                but We mortals were fashioned from the earth, * and unto earth shall we return,
                * as Thou Who fashioned me didst command and say unto me, * “From earth
                thou art and unto earth shall thou return,” * whither all We mortals are going, *
                making our funeral lament the song: * Alleluia, alleluia, alleluia.
                SYNAXARION READING
                Verse: When Thou O judge of all, shall sit to judge the earth.
                Verse: May Thou judge me also, to hear Thy words: “Come hither”.
                On this day, Soul Saturday, according to the order instituted by our Holy
                Fathers, we call to remembrance all those who have died from the beginning of
                the ages in faith and in the hope of the resurrection and of life eternal. The
                present commemoration of the dead is based on the reality that many of our
                fathers and mothers, brothers and sisters died under such circumstances that
                funeral prayers and normal memorial services could not be offered for them.
                Either in a foreign land or on the seas, on impassable mountains or in gulfs or
                precipices, through starvation or diseases, in wars, in fires, or during
                earthquakes, and in so many other ways, perhaps in poverty or in need, our
                known and unknown brothers and sisters in Christ did not enjoy the chanting
                and necessary spiritual care. Therefore, our Holy Fathers, moved by their love
                for humanity, appointed the present celebration to take place in the Church
                everywhere, having received this from the Holy Apostles, so that all who have
                died through various mishaps or accidents may be remembered together, for
                the benefit of their souls. There is great profit to the soul from these memorials
                in the Church. This is the first reason. The second reason is that since the Holy
                Fathers were going to place the memory of Christ’s Second Coming on the
                following day, Sunday, they appropriately commemorate the souls today, as it
                were, propitiating the fearful Judge, who cannot be deceived, to apply His usual
                compassion and to appoint them to the promised delight. Furthermore, the
                Sunday following tomorrow is dedicated to Adam’s exile from Paradise, after
                which a new life is considered to begin for ourselves. Before this new
                beginning, the present memorial service has as its purpose to warn and frighten
                the living, so that they may meditate on their own death and proceed more
                diligently in the spiritual struggles of Great Lent. After their falling asleep, the
                Judgment shall follow by the Judge who cannot be bribed. We always remember
                the souls of the dead on the Sabbath, for the Sabbath (Saturday) is the day of
                rest. In Hebrew, Sabbath literally means “rest.” As the Jews have this day for
                their repose and paused from every work and professional dealing, we
                Christians have it to remember the repose of our those who preceded us. On
                this day, we hold memorial services and have koliva blessed in the church, give
                alms, and perform various works of mercy. All these practices are of great
                benefit to the departed souls. Since the Orthodox Church does not celebrate
                Divine Liturgies on weekdays during Great Lent where the dead can be
                commemorated, the second, third, and fourth Saturdays of the Fast are
                designated as Soul Saturdays. There are many proofs that the souls of the
                departed can be greatly benefited by what is done in their behalf. St. Marcarios
                the Egyptian once saw the dry skull of a pagan by the road on his way, and
                asked, saying, “Do you ever have any kind of consolation in Hades?” And the
                skull answered, “Yes, Father, especially when you pray for the sake of the dead;
                abundant is the comfort which we then enjoy.” The great man became very
                happy, because he always prayed for the dead and wished to be assured of the
                results of his intercessions. Another saint, Gregory the Dialogist, saved the
                Roman Emperor Trajan through his prayers, although he heard from God
                never to pray like that on be half of an impious non Christian again. Also
                Theodora the Empress, by the prayers of the holy men and confessors, saved
                her husband, the iconoclast Emperor Theophilos abhorred by God, from the
                everlasting torments. In his funeral oration to his brother Caesarios, St. Gregory
                the Theologian recommends alms on behalf of the reposed as being good. And
                the great Chrysostom in his commentary on Philippians says, “Let us think of
                ways to benefit the departed. Let us give them what help we can, namely
                almsgiving and offerings. For truly this brings them great advantage and very
                much gain and benefit. The custom of the priest commemorating those reposed
                in faith over the awesome Mysteries has not been without purpose nor
                arbitrarily ordained and delivered to God’s Church by His all-wise Disciples.”
                Again, “In making arrangements when you dispose of your property, together
                with your children and relatives, let your will also include the name of your
                Judge as a joint heir, and let not the mention of the poor be absent. St.
                Athanasius the Great also says that even if one has died and dissolved into the
                air, do not decline to provide oil and candles at the grave and to plead with
                Christ our God, for they are acceptable to God and bring great recompense: if
                the deceased was a sinner, that you may lose his sins; if righteous, that it may
                add to his reward. If one is a stranger without means, having no one to take
                care of these matters, God, being righteous and compassionate, will
                proportionately measure out to him His mercy, as He knows best. Moreover, he
                who offers such services to the dead also partakes of the reward, because he has
                shown love and concern for the salvation of his neighbor. It is as when one
                anoints a friend with perfumes, he receives the sweet aroma first. As for those
                who do not fulfill the wills and testaments of the deceased concerning these
                matters, they will positively be condemned. Until Christ’s Second Coming,
                whatever is done for the souls of the dead is beneficial, as the Fathers say,
                particularly to those who had done some small good deeds when they were
                among the living. Even if the divine Scriptures declare certain things as needed
                for the chastening of the majority, yet as a rule God’s love for man prevails. For
                if the balance of good and shameful deeds is even, God’s love for man prevails.
                If the scale is weighed down a little by evil deeds, again His exceeding goodness
                prevails. In the other life, everyone will be acquainted even with those whom
                they have never seen before, as the divine Chrysostom says, deducing this from
                the parable of the rich man and Lazarus. All will recognize each other, but not
                from any bodily characteristics. For all shall be one age, and traits from birth
                will be absent. Rather, we shall recognize each other through the soul’s spiritual
                eyes, as St. Gregory the Theologian says in his funeral oration to Caesarios:
                “Then I shall see Caesarios, beaming with joy and glorious, such as you have
                often appeared to me in my dreams, O most beloved of brothers.” St.
                Athanasios the Great also says in his homily on the dead that until the time of
                the universal resurrection it has been granted to the saints to recognize each
                other and revel together, while the sinners, on the other hand, have been
                deprived even of this. Regarding the holy martyrs, they are capable of observing
                our actions and even of visiting us. Then all shall know one another when the
                hidden secrets of every man shall be revealed. We should know that, for the
                time being, the souls of the righteous dwell in certain places set aside for them,
                and the souls of the sinners in their own location. The former rejoice in their
                hope, but the latter grieve in expectation of future suffering. Therefore, the
                saints have not yet received the promised blessings, according to the words of
                the Holy Apostle Paul, who says, “God having provided something better for
                us, that they should not be made perfect apart from us” (Heb. 11:40). We
                should also know that not all who have suffered death by various accidents
                (falling down from precipices, being burned in fires, being sunk in seas, or
                perishing by starvation, poison, frost, and so on) have had such an end as a
                result of God’s command. For these are God’s judgments: some occur with His
                approval, others by His permission. Still others occur as a warning, a threat, or a
                chastisement. By foreknowledge He knows and is aware of everything, and
                everything occurs by His will, as with the sparrows about which the Holy
                Gospel speaks. He does not order that, for example, one man is to die by
                drowning and another to die normally, one as an old man and the other as an
                infant. But once and for all He determined, with some exceptions, the general
                times and various kinds of death in man. Within these constraints do the
                various means of death occur, without God’s determining them precisely from
                the beginning, only knowing. But in relation to the life of each and every
                person, God’s will plans the time and the manner of each one’s death. St. Basil
                the Great speaks about the limits of man’s life, although he is alluding to God’s
                words, “For dust you are, and to dust you shall return” (Gen. 3:19). St. Paul also
                writes to the Corinthians, “For he who eats and drinks in an unworthy manner
                eats and drinks judgment to himself, not discerning the Lord’s body. For this
                reason many are weak and sick among you, and many sleep” (1 Cor. 11:29).
                Here the word sleep refers to death. The Holy Prophet David says, “Do not
                take me away in the midst of my days. Your years are throughout all
                generations”(Ps. 101:25). Again, “You have made my days a few spans, and my
                existence is nothing in your sight” (Ps. 38:6). The Holy King Solomon says,
                “son, honor your father, that you may live many years, and not die before your
                time” (Eccles 3:5 - 6). And the Lord himself, speaking to Eliphaz the Temanite,
                says, “For I will accept him, lest I deal with you according to your folly; because
                you have not spoken of Me what is right, as my servant Job has” (Job 42:8).
                Hence it is evident that there is no set term of life. Or, if there is one, it is
                whatever God wills. For as He so wishes He adds to or deletes from the time of
                the life of this or that individual, administering all things for our benefit. And
                when He so wills, God arranges both the place and the time of repose.
                According to St. Athanasios the Great, the term of each person’s life is set by
                the will and counsel of God: “Through the depths of Thy judgments shalt Thou
                care for all, O Christ.” According to St. Basil the Great, death comes as soon as
                the term of life has been fulfilled; by the words term of life, God’s will is meant.
                For if the term of life had already been determined, then for what do we need
                God, or even a physician? And why do we pray for our children? One ought to
                know that baptized infants who die shall enjoy the bliss of Paradise; those not
                baptized and those of the heathen shall go neither to the place of bliss nor to
                Hades. When the soul has left the body, it no longer has any concern for earthly
                things but is continually concerned with matters in the next life. We celebrate
                the first memorial service on the third day after death, because by the third day
                the dead one’s appearance is altered. We serve the second memorial service on
                the ninth day after death, because by this day the entire body is dissolved,
                except for the heart. We serve the third memorial service on the fortieth day,
                for by this day the heart has deteriorated. The same progression, in reverse
                order, is made at birth: by the third day after conception the heart is formed; by
                the ninth day the flesh is fashioned, and by the fortieth day the full form
                appears.
                O Master Christ, set the souls of Your departed servants in the tabernacles
                of Your righteous, and have mercy upon us and save us,
                as You are the only Immortal One. Amen
                ODE VII
                Canon of the temple, then:
                Irmos: O Thou who in the beginning ...,
                Refrain: Wondrous is God in His saints, the God of Israel.
                Celebrating the memory of those who from the ages have passed away in
                the true faith, we cry aloud: Blessed art Thou unto all the ages, O Lord God of
                our fathers.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                Grant rest O God, to the faithful that have fallen asleep, who have perished
                suddenly, struck by some weapon of iron, wood or stone.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                At Thy dread coming, O Compassionate One, place at Thy right hand with
                Thy sheep all those who in life served Thee in the Orthodox faith O Christ, and
                have now departed to Thee.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                Grant to Thy servants, O Christ, a place in the choir of Thine elect, that they
                may cry aloud to Thee: Blessed art Thou throughout the ages, O Lord God of
                our fathers.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                Thou hast fashioned our flesh from the dust of the earth, O merciful Savior,
                and quickened it by the Spirit: grant rest, O God, to those whom Thou hast
                taken, in the life that groweth not old.
                Glory ..., Let us praise the Godhead, one in Nature but threefold in
                Hypostasis, Father, Son and Holy Spirit, three Suns, but singular in light.
                Now & ever ..., Theotokion: With the words of David we sing to thee in
                unison, O Virgin, calling thee the mountain of God: for the Word dwelt within
                thee in the flesh, wherein He spiritually rendered our nature godlike.
                Katavasia: O Thou who in the beginning founded the earth * and by Thy
                word made the heavens firm, * blessed art Thou throughout the ages, *
                O Lord God of our Fathers.
                ODE VIII
                Canon of the temple, then:
                Irmos: Glorified in the holy mountain ...,
                Refrain: Wondrous is God in His saints, the God of Israel.
                Thou hast destroyed the shadow of death of old, and shone forth from the
                tomb as the rising sun: O Lord of glory, make all those from every age who
                died in faith sons of Thy Resurrection.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                Thou who knowest things obscure and hidden, when Thou shalt come to
                reveal the works of darkness and the counsels of our hearts, then exact not
                what is due of all who have fallen asleep in faith,.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                When Thou shalt come to sit upon the throne and shalt summon with the
                trumpet all mankind from the ends of the earth, commanding them to stand
                before Thee for judgment, then spare us all, O Christ, in that Thou art merciful.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                Those of the faithful who died suddenly by accident, crying out violently,
                and running swiftly, or were struck on the face or trampled underfoot, do Thou
                forgive, O Lord of glory, unto the ages.
                Verse: We bless the Father, Son and Holy Spirit, the Lord.
                As a Unity in Essence I sing Thy praises; as a Trinity in Hypostases I
                venerate Thee, Father, Son and Most holy Spirit. The power of Thy
                beginningless Kingdom do I glorify throughout the ages.
                Now & ever ..., Theotokion: Thou hast been revealed, O Virgin Theotokos,
                as a sealed fountain of living water. For without man thou hast given birth to
                the Lord, and thou dost grant the faithful to drink from the waters of
                immortality throughout the ages.
                Verse: We praise, bless and worship the Lord ...,
                Katavasia: Glorified in the holy mountain, * the Lord revealed the
                mystery of the Ever-Virgin unto Moses * in the flames of the burning
                bush: * praise ye and supremely exalt Him throughout all ages.
                ODE IX
                Canon of the temple, then:
                Irmos: The prophetic vision of the lawgiver ...,
                Refrain: Wondrous is God in His saints, the God of Israel.
                Where Thy saints dwell in joy, O Lord, grant that all from every age who
                have fallen asleep in the faith, and in hope, may also rejoice.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those who have died by the wrath of God: struck down by thunderbolts
                from heaven, swallowed by the earth, or drowned in the sea; to all the faithful
                grant rest, O Christ
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those from every age in life: old and young, children and the suckling
                new-born, male and female. To all the faithful Thou hast taken Grant rest, O
                God.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                To those killed by poisonous bites, swallowed by serpents, trampled
                underfoot by horses, strangled or hanged by their neighbors. Grant rest to all
                who worshipped Thee in faith.
                Refrain: Grant rest, O Lord, to the souls of Thy departed servants.
                We remember by name each of the faithful who died in every generation
                from the ages: grant that, at Thy coming, they may stand before Thee
                uncondemned.
                Glory ..., O God, One in Three, glory be to Thee without ceasing. For each
                is God, yet Father, Son and Spirit are one in Nature, a threefold radiant
                distinctness.
                Now & ever ..., Theotokion: Thy childbearing transcends understanding,
                for thou hast given birth to Him who was before all that is, and with milk
                ineffably fed Him who feedeth the whole world, and held Him who doth
                uphold the universe, Christ our only Redeemer, O all-immaculate One.
                Katavasia: The prophetic vision of the lawgiver on the mountain, * in the
                fire of the burning bush, * prefigured thy birthgiving O Ever-Virgin, * the
                salvation of us the faithful, * wherefore with never silent hymns we
                magnify thee.
            """
            ,'exapostilarion': """
                Exapostilarion, in Tone III;
                As Thou art God Who hast authority over both the living and the dead, *
                grant rest to Thy servants in the dwelling-place of the elect, * for though they
                have sinned, O Savior, ** yet they turned not away from Thee.
                Glory ..., Grant rest to Thy servants, O Lord, in the land of the living * from
                which have fled pain, sorrow and sighing. * O Lover of mankind be merciful to
                the sins that they committed in this life: * for Thou alone art sinless and
                merciful, ** O Master of the dead and the living.
                Now & ever ..., Theotokion: O Mary, Bride of God, pray without ceasing
                unto Christ * on behalf of us thy servants, * that with the prophets inspired by
                God, * and the companies of the martyrs, * of hierarchs, holy monks and all the
                righteous, ** we may become fellow-heirs of the Kingdom of Heaven.
            """
            ,'praises':"""
                In Tone VIII:
                Spec. Mel.: “The Paradise in Eden ...”:
                Come, all ye brethren, before the end, * and let us all look upon our form, *
                upon the infirmity, and callousness of our nature. * Let us behold our end, and
                the organs of the vessel of our flesh. * Let us see that man is but dust, food for
                worms, and corruption; * that our bones grow dry, and have no breath of life in
                them. * Let us gaze on the tombs. * Where is man’s glory? Where his outward
                beauty? * Where the eloquent tongue? Where the noble brow, * and where the
                eye? * All is but dust and a shadow. ** Therefore, O Savior, spare us all.
                Why doth man deceive himself and boast? * Why doth he trouble himself in
                vain? * For he is but earth, and soon to the earth will he return. * Why doth the
                dust not reflect upon its formation from clay, * and that it shall be cast out as
                dung and corruption? * Yet though We men are but clay, why do we cling so
                closely to the earth? * For if we are Christ’s kindred, should we not run to Him,
                * leaving this mortal and fleeting life, * and seek life incorruptible, ** which is
                Christ Himself, the illumination of our souls?
                Thou hast formed Adam with Thine own hand, * and placed him on the
                border between incorruption and mortality, O Savior, * and granting him life
                through grace, Thou hast freed him from corruption, * translating him to the
                life that he first enjoyed. * Grant rest, O Master, to Thy servants whom Thou
                hast taken from us; * may they rest with the righteous in the choir of Thine
                elect; * write their names in the book of life; raise them with the sound of the
                Archangel’s trump, ** and grant them Thy heavenly Kingdom.
                Christ is risen, releasing from bondage Adam the first-formed man * and
                destroying the power of Hades. * Be of good courage, all ye dead, * for death is
                slain and Hades despoiled; * and Christ hath assumed Kingship. * He hath
                granted incorruption to our flesh; * He hath raised us and granted us
                resurrection, * and He doth make worthy of His joy and glory ** all who, with
                unwavering faith, fervently trust in Him.
                Glory ..., in Tone II:
                As a flower withereth and a dream passeth away, * so is each man’s flesh
                dissolved at death. * But at the sound of the trumpet all the dead, * as in an
                earthquake, * shall rise again to meet Thee, Christ God. * Then, Master, grant
                unto all Thy servants * whom Thou hast taken from us, ** to dwell in the
                tabernacles of Thy saints.
                Now & ever ..., Theotokion, in Tone II:
                Rejoice, O Theotokos Mary, * thou indestructible and surpassingly holy
                temple; * as the prophet crieth out: ** Holy is thy temple, wondrous in
                righteousness!
            """
            ,'aposticha_theotokion': """
                Glory ..., for the reposed, by St. John of Damascus, in Tone VI:
                By eating from the tree * Adam was brought to grief in the days of old in
                Eden, * through the poison of the serpent; * for in this way death entered, *
                devouring the whole race of mankind. * But the Master by His coming * hath
                destroyed the dragon and bestowed upon us rest. * To Him, therefore, let us cry
                aloud: * Spare, O Savior, those whom Thou hast taken, ** and grant them rest
                with Thine elect.
                Now & ever ..., Theotokion, in Tone VI:
                Thou art our God, Who in Wisdom * hath created and perfected all things.
                * Thou hast sent prophets, O Christ, to foretell Thine advent, * and apostles to
                proclaim Thy majesty; * the former prophesied of Thy coming, * and the later
                illumined the nations by baptism, * while the martyrs through their sufferings
                received their expectation. * With Her who gave birth to Thee, * they all
                intercede before Thee: * Do Thou grant rest, O God, * to the souls of those
                whom Thou hast taken; * and, deem us worthy of Thy Kingdom, * O my
                Redeemer and my God, * Who didst endure the Cross on my behalf, ** the
                condemned one.
            """
            ,'apolytichia':"""
                In Tone VIII:
                O Thou Who by the depth of Thy wisdom * dost provide all things out of
                love for man, * and grantest unto all that which is profitable, O only Creator: *
                Grant rest, O Lord, to the souls of Thy servants; ** for in Thee have they
                placed their hope, O our Creator and Fashioner and God.
                Glory ..., Now & ever ..., Theotokion:
                In thee do we have a rampart and calm haven * and an intercessor
                acceptable to God, ** Whom thou didst bear, O Theotokos unwedded, thou
                salvation of the faithful.
            """
        } #Matins
        ,'liturgy': {
            'beatitudes': [
                """
                    To those who have passed through the course of this life in the glory of
                    piousness, do Thou O God, make worthy to be adorned with a crown of
                    righteousness, and may they enjoy eternal blessings.
                """
                ,"""
                    To those who have been suddenly snatched away, burnt by lightning, frozen
                    by cold, or struck down by any other calamity, grant rest, O God, when Thou
                    shalt try all things by fire.
                """
                ,"""
                    To those who have sailed across the ever-troubled sea of this life, grant safe
                    anchorage O Christ, in the harbor of immortal life with Thee, nurtured by an
                    Orthodox life.
                """
                ,"""
                    Those whom the creatures of the sea or the birds of the air have devoured,
                    by Thy judgments O Christ God, raise up in glory on the Last Day
                """
                ,"""
                    Thou hast loosed the pains of death, having suffered <the Passion>, O our
                    God, Thou author of Life: grant rest to Thy servants who have fallen asleep
                    from the ages
                """
                ,"""
                    To those whom, according to Thine inscrutable judgments, Thou hast
                    permitted to be slain by drugs or by poison, or through choking on bones, grant
                    rest, O Lord, with Thy saints
                """
                ,"""
                    Glory ..., Thrice-holy Godhead, One in throne, Father, Son and Spirit, Thou
                    art my God, holding all in unity by Thine almighty Power.
                """
                ,"""
                    Now & ever ..., Theotokion: Leap for joy, O Jesse the forefather; for from
                    thy root hath Sprung forth the Flower of Life that saveth the world, Christ God
                    born from the pure Maiden.
                """
            ]
            ,'troparion':"""
                The Troparion of the day, in Tone VIII);
                O Thou Who by the depth of Thy wisdom dost provide all things out of
                love for mankind, and grantest unto all that which is profitable, O only Creator:
                Grant rest, O Lord, to the souls of Thy servants; for in Thee have they placed
                their hope, O Creator and Fashioner and God.
            """
            ,'kontakion': """
                Kontakion for the day in Tone VIII:
                Glory ..., With the Saints grant rest, O Christ, * to the souls of Thy servants,
                * where there is neither * pain, nor sorrow, nor sighing, * but life everlasting.
                Theotokion, in Tone VIII:
                Now & ever ..., In thee do we have a rampart and calm haven * and an
                intercessor acceptable to God, Whom thou didst bear, ** O Theotokos
                unwedded, thou salvation of the faithful.
            """
            ,'prokeimenon':"""
                Prokeimenon, in Tone VI:
                Prokeimenon: Their souls * shall dwell among good things.
                Verse: Unto Thee, O Lord, have I lifted up my soul: my God, I have put my
                trust in Thee
            """
            ,'readings': """
                1st EPISTLE TO THE CORINTHIANS (10:23-28)
                Brethren: All things are lawful for me, but all things are not expedient: all
                things are lawful for me, but all things edify not. Let no man seek his own, but
                every man another’s wealth. Whatsoever is sold in the shambles, that eat, asking
                no question for conscience sake: For the earth is the Lord’s, and the fullness
                thereof. If any of them that believe not bid you to a feast, and ye be disposed to
                go; whatsoever is set before you, eat, asking no question for conscience sake.
                But if any man say unto you, This is offered in sacrifice unto idols, eat not for
                his sake that shewed it, and for conscience sake: for the earth is the Lord’s, and
                the fullness thereof:
                1st EPISTLE TO THE THESSALONIANS (4:13-17)
                Brethren: I would not have you to be ignorant, concerning them which are
                asleep, that ye sorrow not, even as others which have no hope. For if we believe
                that Jesus died and rose again, even so them also which sleep in Jesus will God
                bring with him. For this we say unto you by the word of the Lord, that we
                which are alive and remain unto the coming of the Lord shall not prevent them
                which are asleep. For the Lord himself shall descend from heaven with a shout,
                with the voice of the archangel, and with the trump of God: and the dead in
                Christ shall rise first: Then we which are alive and remain shall be caught up
                together with them in the clouds, to meet the Lord in the air: and so shall we
                ever be with the Lord.
                THE GOSPEL ACCORDING TO ST. LUKE (21 : 8-9, 25-27, 33-36)
                The Lord spake unto His disciples saying: Take heed that ye be not
                deceived: for many shall come in my name, saying, I am Christ; and the time
                draweth near: go ye not therefore after them. But when ye shall hear of wars
                and commotions, be not terrified: for these things must first come to pass; but
                the end is not by and by. And there shall be signs in the sun, and in the moon,
                and in the stars; and upon the earth distress of nations, with perplexity; the sea
                and the waves roaring; Men’s hearts failing them for fear, and for looking after
                those things which are coming on the earth: for the powers of heaven shall be
                shaken. And then shall they see the Son of man coming in a cloud with power
                and great glory. Heaven and earth shall pass away: but my words shall not pass
                away. And take heed to yourselves, lest at any time your hearts be overcharged
                with surfeiting, and drunkenness, and cares of this life, and so that day come
                upon you unawares. For as a snare shall it come on all them that dwell on the
                face of the whole earth. Watch ye therefore, and pray always, that ye may be
                accounted worthy to escape all these things that shall come to pass, and to stand
                before the Son of man.
                THE GOSPEL ACCORDING TO ST. JOHN (5: 24-30)
                The Lord spake unto the Jews who came unto Him, saying: Verily, verily, I
                say unto you, He that heareth my word, and believeth on him that sent me, hath
                everlasting life, and shall not come into condemnation; but is passed from death
                unto life. Verily, verily, I say unto you, The hour is coming, and now is, when
                the dead shall hear the voice of the Son of God: and they that hear shall live.
                For as the Father hath life in himself; so hath he given to the Son to have life in
                himself; And hath given him authority to execute judgment also, because he is
                the Son of man. Marvel not at this: for the hour is coming, in the which all that
                are in the graves shall hear his voice, And shall come forth; they that have done
                good, unto the resurrection of life; and they that have done evil, unto the
                resurrection of damnation. I can of mine own self do nothing: as I hear, I judge:
                and my judgment is just; because I seek not mine own will, but the will of the
                Father which hath sent me.
            """
        } #Liturgy
    } #Service
    ,'-56': { #Meatfare Sunday
        'vespers': {
            'stichera_tone': 'in Tone VI:'
            ,'stichera': [
                """
                    When Thou shalt come, O most righteous Judge, * to execute the just
                    judgment, * seated on Thy throne of glory, * the frightening river of fire will
                    draw all mankind * before Thy judgment seat; * the heavenly powers will stand
                    beside Thee, * and in fear mankind will be judged according to the deeds that
                    each has done. * With faith we entreat Thee O Christ, * since Thou art
                    compassionate * spare us then, and grant us a place among those who are saved.
                """
                ,"""
                    The books will be opened * and the deeds of all mankind will be revealed *
                    before the dread judgment seat; * the whole vale of sorrow shall echo * with the
                    fearful and despairing sounds of lamentation, * at seeing all who have sinned
                    being sent by Thy just judgment * to everlasting torment, weeping in vain. *
                    Therefore we beseech Thee, O compassionate One: * Spare us who hymn Thy
                    praises, ** for Thou alone art plenteous in mercy.
                """
                ,"""
                    The trumpets shall sound and the tombs shall be emptied, * and all mankind
                    shall be raised in trembling. * Those that have done good shall rejoice in
                    gladness, * awaiting to receive their reward; * those that have sinned shall
                    tremble and in grief lament, * as they are separated from the chosen and sent to
                    torment. * O Lord of glory, be merciful to us as Thou art compassionate, ** and
                    grant us to dwell * with those that have loved Thee.
                """
                ,"""
                    I lament and weep when I contemplate the eternal fire, * the outer darkness
                    and Tatar, * the dread worm and the unceasing gnashing of teeth, * and the
                    anguish that shall befall those who have sinned immeasurably, * by their
                    wickedness arousing Thee to anger O supremely good One. * Among them I,
                    the miserable one, am first: ** But, O Judge in Thy mercy save me, for Thou art
                    lovingly compassionate.
                """
            ]
            ,'doxastichon': """
                    in Tone VIII:
                    When the thrones are set-up and the books opened, * and God siteth in
                    judgment, * O what fear there shall be then, * with the angels standing in Thy
                    presence trembling * and the river of fire flowing before Thee, * what shall we
                    do then, who are guilty of a multitude of sins? * When we hear Him calling the
                    blessed ones of His Father into the Kingdom, * but sending sinners to torment. *
                    Who shall endure His fearful condemnation? * But, O Savior Who alone lovest
                    mankind, * King of the ages, * before the end cometh ** turn me back through
                    repentance and have mercy on me.
            """
            ,'aposticha_theotokion': """
                    Glory ..., from the Triodion, in Tone VIII:
                    Alas, O darkened soul! * How long wilt thou turn not away from
                    wickedness? * How long wilt thou recline in idleness? * Why dost thou not think
                    of the fearful hour of death? * Why dost thou not tremble at the dread judgment
                    seat of the Savior? * What answer wilt thou give then, or what wilt thou say? *
                    Thy works will stand in accusation of thee; * thine actions will reproach thee and
                    condemn thee. * O my soul, the time draweth near; * make haste before it is too
                    late, and cry aloud in faith: * “I have sinned, O Lord, I have sinned against Thee;
                    * but I know O Lover of mankind, Thy compassion, * deprive me not O good
                    Shepherd, of a place at Thy right hand ** for the sake of Thy great and abundant
                    mercy”.
                    Now & ever ..., in Tone VIII:
                    O unwedded Virgin! * thou who ineffably conceived God in the flesh, *
                    Mother of God Most High: * accept the supplications of thy servants, O allimmaculate one, * granting unto all cleansing of transgressions; * and, accepting
                    now our supplications, ** pray thou that we all be saved.
            """
        } #Vespers
        ,'matins': {
            'after50': """
                in Tone VIII:
                Glory ..., The gates of repentance, do Thou open unto me, O Giver of Life,
                * for early in the morning my spirit seeketh Thy holy temple, * bearing the
                temple of my body all defiled. * But as One who art compassionate * cleanse it
                by Thy loving-kindness and mercy.
                Now & ever ..., Guide me on the paths of salvation, O Theotokos: * for I
                have polluted my soul with shameful deeds * and wasted all my life in
                slothfulness. * but by thine intercessions * do thou deliver me from all impurity.
                In Tone VI:
                Have mercy upon me, O God, * according to Thy great mercy: * and
                according to the multitude of Thy compassion * blot out my transgressions.
            """
            ,'canon': """
                ODE I
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: A helper and a protector hath become unto me ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I tremble with fear when I contemplate the dread day of Thine ineffable
                coming, I fear when I foresee Thee sitting in judgment of the living and the dead,
                O mine all-powerful God.
                Refrain: Have mercy on me, O God, have mercy on me.
                When Thou shalt come, O God, with thousands of the heavenly hosts of
                angels, deem me the wretched one O Christ, worthy to meet Thee in the clouds.
                Refrain: Have mercy on me, O God, have mercy on me.
                Come, O my soul, and call to mind the very hour and day when God shall
                stand before thee visibly; lament and weep, and thus be found pure in the hour
                of the trial.
                Refrain: Have mercy on me, O God, have mercy on me.
                The unquenchable fire of Gehenna, the bitter worm and the gnashing of
                teeth, terrorize me and fill me with awe. But do Thou O Christ, release me and
                forgive me, and number me among Thine elect.
                Refrain: Have mercy on me, O God, have mercy on me.
                Grant that I, wretched as I am, may hear Thy greatly desired voice, which
                doth call Thy saints to joy, that I also may attain the inexpressible enjoyment of
                the Kingdom of Heaven.
                Refrain: Have mercy on me, O God, have mercy on me.
                Enter not into judgment with me, recalling my deeds, examining my words
                and correcting my urgings. But in Thy compassion overlook my wickedness and
                save me, O all-powerful One.
                Glory ..., Unity in three Hypostasis, Sovereign Lord of all, perfect and
                beginningless God, the Father, Son and most holy Spirit, save us.
                Now & Ever ..., Who, according to the law of nature, hath ever begotten a
                son not sown by a father? Yet such a Son the Father hath begotten without a
                mother. O most wondrous marvel! For thou O pure One, hast borne both God
                and man.
                Katavasia in Tone VI: A helper and a protector * hath become unto me
                salvation. * My God, whom I will glorify, * the God of my fathers, * and I
                will exalt Him * for gloriously hath He been glorified.
                ODE III
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: O Lord, upon the rock of Thy commandments ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                The Lord cometh, and who shall endure the fear of Him? Who shall dare
                appear before Him? But do thou prepare thyself to meet Him, O my soul.
                Refrain: Have mercy on me, O God, have mercy on me.
                Let us make haste before it is too late; let us lament, let us be reconciled to
                God before the end. For fearful is the judgment at which all of us shall stand
                naked.
                Refrain: Have mercy on me, O God, have mercy on me.
                Have mercy, O Lord, have mercy upon me, I cry to Thee, when Thou
                comest with Thine angels to render to every man his due reward for his deeds.
                Refrain: Have mercy on me, O God, have mercy on me.
                How shall I endure the wrath of Thy judgment, for I have not hearkened
                unto Thy commandments? But spare, O spare me in the hour of judgment.
                Refrain: Have mercy on me, O God, have mercy on me.
                Turn back, O wretched soul, sighing, before the fair-ground of life cometh
                to an end, before the Lord shuteth the door of the bridal chamber.
                Refrain: Have mercy on me, O God, have mercy on me.
                O Lord, I have sinned as no other man hath sinned, I have transgressed
                more than any man: before the day of judgment, be merciful to me O Lover of
                mankind.
                Glory ..., O simple Unity praised in a Trinity of Hypostases, uncreated
                beginningless Nature, save us who in faith worship Thy power.
                Now & Ever ..., O most pure One, by a seedless conception thou hast given
                birth to the living Word, Who without change assumed flesh in thy womb. Glory
                be to thy birthgiving, O Mother of God.
                Katavasia: O Lord, upon the rock of Thy commandments * make firm my
                fickle heart, * for Thou alone art Holy and Lord.
                Sessional Hymns from the Triodion, in Tone VI:
                When I contemplate the fearful day, * and weep over my evil deeds, * how
                shall I answer the immortal King, * with what justification shall I look upon the
                Judge, * prodigal that I am. * O compassionate Father, * only begotten Son, and
                Holy Spirit, ** have mercy on me.
                Glory ..., O what lamentation there will be in that place, * when Thou, O
                compassionate One, * dost sit to execute Thy righteous judgment; * disclose not
                my secret sins, * nor shame me before the Angels, ** but be compassionate O
                God and have mercy on me.
                Now & ever ..., O thou good Virgin Theotokos, * the hope of the world, *
                we beg thine intercession which alone is mighty: * have compassionate mercy
                upon us, * a people bereft of an intercessor; * beseech the merciful God, that our
                souls be delivered from every threat, ** O thou who alone art blessed!
                ODE IV
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: The prophet heard of thy coming, O Lord, ...
                Refrain: Have mercy on me, O God, have mercy on me.
                The day is upon us, the judgment is at the door. Be vigilant, my soul, Kings
                and princes, rich and poor are gathering and each shall receive their due reward
                for their actions.
                Refrain: Have mercy on me, O God, have mercy on me.
                Each in his own order, monk and hierarch, old and young, slave and master
                shall be examined; widow and virgin shall be corrected. And woe to all whose
                lives are not guiltless!
                Refrain: Have mercy on me, O God, have mercy on me.
                Thy judgment is without respect of persons; no cunning words or eloquence
                can deceive it; nor shall false witnesses pervert Thy righteousness. For in Thy
                sight, O God, every secret shall stand revealed.
                Refrain: Have mercy on me, O God, have mercy on me.
                Let me not come into the valley of lamentation, let me not see the place of
                darkness, O my Christ and Word; let me not be bound hand and foot, and cast
                out from Thy bridal chamber, for in my utter wretchedness I have defiled the
                garment of incorruption that hath been given me.
                Refrain: Have mercy on me, O God, have mercy on me.
                When Thou shalt separate the sinners from the righteous whilst judging the
                world, number me as one of Thy sheep and place me not with the goats, O
                Lover of mankind, that I may hear the voice of Thy blessing.
                Refrain: Have mercy on me, O God, have mercy on me.
                When the trial taketh place and the books recording all our deeds shall be
                opened, O miserable soul, what shalt thou answer before the judgment-seat,
                lacking all fruits of righteousness to offer unto Christ thy Creator?
                Refrain: Have mercy on me, O God, have mercy on me.
                Hearing the words of lamentation of the rich man in the flames of torment,
                I, the wretched one, weep and wail, for I am deserving of the same
                condemnation. Wherefore I entreat Thee: Have mercy on me, O Savior of the
                world, at the hour of judgment.
                Glory ..., I glorify the Son Who hath come forth from the Father, and the
                Spirit, as light and rays from the Sun: the One begotten as an Offspring, the
                Other proceeding and sent forth; divine and coeternal Trinity, worshiped by all
                creation.
                Now & Ever ..., She who hath given birth yet kept her virginity, hath borne
                both God and man, a single Person with a twofold nature. This thy miracle, O
                Virgin Mother, doth fill every ear and mind with wonder.
                Katavasia: The prophet heard * of Thy coming, O Lord, * and he was
                afraid. * How wast Thou to be born of a virgin * and appear unto
                mankind? * and he said * “I have heard report of Thee and I am afraid”; *
                glory to Thy power, O Lord.
                ODE V
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Out of the night I seek Thee early ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                There shall be fear and trembling beyond all description there: for the Lord
                shall come and test the works of every man. And who then will not mourn for
                himself?
                Refrain: Have mercy on me, O God, have mercy on me.
                The river of fire disquietens and consumes me; the gnashing of teeth grinds
                me, and the abyss dismays me, how or what shall I do to gain God’s mercy?
                Refrain: Have mercy on me, O God, have mercy on me.
                Spare, O Lord, spare Thy servant; deliver me not unto the bitter tormentors,
                unto the cruel angels in Hades, by whom I shall never find rest.
                Refrain: Have mercy on me, O God, have mercy on me.
                Prince and governor together, the rich and the inglorious, great and small
                alike will be tried. Woe unto him that hath not prepared himself beforehand!
                Refrain: Have mercy on me, O God, have mercy on me.
                Pardon, remit and forgive, O Lord, all my sins against Thee; and show me
                not condemned, in the presence of the angels, to the punishment of fire and
                unending shame.
                Refrain: Have mercy on me, O God, have mercy on me.
                Spare, O spare the Thy creation, O Lord. I have sinned, forgive me: for
                Thou alone art pure by nature, and none save Thee is free from defilement.
                Glory ..., A single Unity by nature, I praise Thee O Trinity, as beginningless,
                incomprehensible, supreme in sovereignty, a unity beyond perfection, God, Light
                and Life, the Creator of the world.
                Now & Ever ..., In thy childbearing, in a supra-natural manner, the laws of
                nature were rendered mute, O pure one. For without seed thou hast given birth
                to the pre-eternal God, begotten from the Father.
                Katavasia: Out of the night I seek Thee early, * enlighten me I pray Thee,
                O Lover of mankind, * and guide me in Thy commandments, * and teach
                me, O Savior, * to do Thy will.
                ODE VI
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: With my whole heart, I cried ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                At Thy fearful coming, O Christ, when Thou shall appear from heaven and
                set up the thrones, and the books shall be opened, then spare, O Savior, spare
                Thy creature.
                Refrain: Have mercy on me, O God, have mercy on me.
                Since God is the Judge, nothing can help thee there, no zeal, no skill, no
                glory, no friendship, but only the strength that thou hast gained, O my soul, from
                thy works.
                Refrain: Have mercy on me, O God, have mercy on me.
                There will be found together both Prince and governor, rich and poor O my
                soul; no father or mother will be able to help us, no brother will deliver us from
                the condemnation.
                Refrain: Have mercy on me, O God, have mercy on me.
                Think, my soul, of the fearful examination before the Judge; trembling from
                this prepare thy defense, lest thou be condemned to the eternal chains.
                Refrain: Have mercy on me, O God, have mercy on me.
                O Lord, may I not hear Thee say, “Take what is due thee,” as Thou dost
                send me from Thy presence; neither let me hear Thee say, “Depart from Me into
                the fire of the accursed,” but may I hear those words desired by the righteous.
                Refrain: Have mercy on me, O God, have mercy on me.
                Deliver me, O Lord, from the gates of Hades, from the lowest depths of the
                earth and the lightless darkness, from the unquenchable fire, and from all the
                other everlasting torments.
                Glory ..., I sing the praises of the Triune Godhead, the Father, Son and
                divine Spirit, one sovereign Principle divided in three Hypostases.
                Now & Ever ..., Thou art the gate through which God alone hath passed,
                entering in and coming out, yet not breaking the seal of thy virginity O pure one:
                Jesus, the Creator of Adam, and thy Son.
                Katavasia: With my whole heart, I cried * unto the all-compassionate God,
                * and he heard me * from the lowest depths of Hades; * and raised up my
                life from corruption.
                Kontakion from the Triodion, in Tone I:
                When Thou comest, O God, upon the earth with glory, * the whole world
                will tremble. * The river of fire will flow before Thy judgment seat, * the books
                shall be opened and secrets revealed. * Deliver me then, from the unquenchable
                fire, ** and deem me worthy to stand on Thy right hand, O Judge most
                righteous.
                Ikos: Thinking of Thy fearful judgment-seat and the day of Judgment O
                supremely good One, I tremble and am filled with fear, for mine own conscience
                accuseth me. No-one then will be able to deny their sins, for truth shall accuse
                them, and fear will constrain them. For great will be the trepidation from the
                flames of Gehenna there, the sinners gnashing their teeth. Wherefore, before the
                end have mercy on me, and spare me, O Judge most righteous.
                SYNAXARION READING
                Verse: When Thou shalt sit to judge the world, O Judge of All.
                Verse: Count me worthy of Thy summons to Thy right hand.
                On this day we commemorate the inescapable second coming of Christ,
                ordained by the most divine Fathers to be observed after the second parable of
                the Prodigal, so that no one who has learned of the love of God for mankind
                from it will live in laziness saying, “God loves mankind, and when I am separated
                from Him by sin, all is prepared for my restoration.” This fearsome day of
                judgment has been designated for commemoration at this point in time, that
                through fear of death and the expectation of future torment, those who live in
                laziness may be encouraged to the virtues, not trusting only in the love of God,
                but also realizing that He is the righteous Judge who will judge all men according
                to their deeds. In other words those souls who have passed over are obliged to
                undergo judgment. And this present feast is a type of symbol of this in that it is
                presented now as a final celebration just as it will be the last event after our
                death. For it behooves us to contemplate that as the beginning of the world and
                Adam’s fall from Paradise are commemorated on the following Sunday, so this
                day is the end of all days and of the world itself. The commemoration is
                appointed for this day of Meatfare, that in awe of this event we should limit our
                intake of earthly food, not giving ourselves over to gluttony, and be encouraged
                to love our neighbor. In other words, since we were banished from Eden, cursed
                and condemned through eating of the fruit, so the present event has been
                ordained at this time, as next Sunday we will be banished through Adam, until
                Christ comes again to raise us up to Paradise. It is called the second coming,
                since Christ appeared to us at His first coming in the flesh and delivered the
                human race, and He will come again to judge whether that which He
                commanded us has been observed. And when will this second coming occur? No
                one knows; for although He mentioned several preceding signs, the Lord
                concealed it from His Apostles. Before His coming the antichrist will appear. He
                will live his life after the manner of Christ, performing miracles like those which
                Christ performed, and raising the dead. Yet all that he does will be an illusion.
                After this suddenly like lightning from heaven the Lord will come, going before
                His holy Cross, and a river of boiling fire will go before Him, cleansing the earth
                of its defilement. The antichrist will be seized immediately along with his
                servants and will be committed to eternal fire. And when the angels sound the
                trumpets, all the nations of mankind will gather from all places and from all the
                ends of the earth in Jerusalem, for it is the center of the earth. And there the
                thrones will be set for judgment. Then all souls will be reunited with their bodies
                and clothed in incorruptible beauty, transformed into one likeness. And with one
                word the Lord will separate the righteous from the sinners. Those who have
                done good will receive eternal life, and the sinners will be once more sent to
                eternal and everlasting torment. Let it be noted that Christ will not ask who
                fasted, or who was naked, or who performed miracles, for although these things
                are good, mercy and compassion are far better. He will question both the
                righteous and the sinners on six commandment-like virtues, of which everyone is
                capable: “For I was hungry, and ye gave me to eat. I was thirsty, and ye gave me
                drink. I was a stranger, and ye took me in; naked, and ye clothed me. I was sick,
                and ye visited me. I was in prison, and ye came to me. Inasmuch as ye have done
                it to one of the least of these my brethren, ye have done it to me.” Then all will
                confess the Lord Jesus Christ in the glory of God the Father. Now the torments,
                according to the Holy Gospel are weeping and the gnashing of teeth, where their
                worm dies not and the fire is not quenched, and he shall be cast into outer
                darkness. For all the Church of God will joyfully delight in attaining the
                Kingdom of Heaven, being close to God in His holy place, and receiving
                everlasting glory and exaltation. But those who are separated from God through
                wasting the life of their souls in laziness and temporal nourishment will receive
                torment and darkness, and be eternally deprived of the divine radiance.
                In Thine ineffable love for mankind, O Christ our God, make us worthy of Thy
                voice, which we long to hear, number us among those at Thy right hand, and
                have mercy on us. Amen.
                ODE VII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: We have sinned, and we have transgressed ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                O ye faithful, let us fall down and lament before the day of judgment doth
                come, when the heavens shall be destroyed, the stars shall fall and all the earth
                shall be shaken, that at the end we may receive mercy from the God of our
                fathers.
                Refrain: Have mercy on me, O God, have mercy on me.
                The trial shall be without respect of persons, and the judgment shall be
                fearful; nothing shall be kept secret from the Judge, no favor can be won with
                bribes. But spare me, O Master, and deliver me from all Thy fearful wrath.
                Refrain: Have mercy on me, O God, have mercy on me.
                The Lord doth come to judge: who can endure the sight of Him? Tremble,
                O my wretched soul, tremble and by thy deeds prepare for thy repose, that thou
                mayest gain mercy and compassion from the blessed God of thy fathers.
                Refrain: Have mercy on me, O God, have mercy on me.
                I am disquieted when I think of the unquenchable fire. The bitter worm, the
                gnashing of teeth, and soul-destroying Hades doth terrify me; yet there is no
                compunction to be found in me. But O Lord, O Lord, before the end, establish
                me in the fear of Thee.
                Refrain: Have mercy on me, O God, have mercy on me.
                I fall down before Thee, and I offer Thee as tears my words. I have sinned
                as the harlot never sinned, and I have transgressed as no other on earth. But O
                Master have compassion upon me Thy creature, and call me back.
                Refrain: Have mercy on me, O God, have mercy on me.
                Turn back O soul, repent, and uncover all that thou hast hidden. Say unto
                God to Whom all things are known: Thou alone knowest my secrets, O Savior;
                do Thou Thyself have mercy on me, as David doth sing, according to Thy
                mercy.
                Glory ..., I sing the praises of the Three, one in Essence, of the One that is
                three in Hypostases: the Father, Son and Holy Spirit, one power, one will, one
                energy, one thrice-holy God, one sovereign Kingdom.
                Now & Ever ..., God hath come forth in beauty from the chamber of thy
                womb. As a King clothed in a divinely-woven robe dyed mystically in thy most
                pure blood, O unwedded one, He doth reign over the earth.
                Katavasia: We have sinned, we have transgressed, * and we have done evil
                before Thee. * We have not kept nor followed * Thy commandments, but
                reject us not utterly, * O God of our fathers.
                ODE VIII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Him whom the hosts of heaven glorify
                Refrain: Have mercy on me, O God, have mercy on me.
                O Lord, when I contemplate meeting Thee at Thy fearful second coming, I
                tremble in awe, and fear Thy wrath. In that hour deliver me, I cry, and save me
                throughout the ages.
                Refrain: Have mercy on me, O God, have mercy on me.
                Who among those born on earth, beset by the passions, shall dare to stand
                before Thee O God who judgeth all things? For at that time, the unquenchable
                fire and the gnawing worm shall seize the condemned and hold them throughout
                the ages.
                Refrain: Have mercy on me, O God, have mercy on me.
                All that has breath, shalt Thou call together to be judged O Christ. Then
                great shall be the fear, and great the anguish; and only our good actions shall help
                us throughout the ages.
                Refrain: Have mercy on me, O God, have mercy on me.
                O my God and Lord, Judge of all, on that day may I hear Thy desired voice,
                may I see Thy great light, may I look upon Thy tabernacles, may I behold Thy
                glory and rejoice throughout the ages.
                Refrain: Have mercy on me, O God, have mercy on me.
                O righteous Judge and Savior, have mercy on me and deliver me from the
                fire and from the punishments I deserve at the Judgment. Before the end
                cometh, grant me remission through virtue and repentance.
                Refrain: Have mercy on me, O God, have mercy on me.
                When Thou sittest in judgment, O compassionate One, and revealest Thy
                dread glory, O Christ, what fear there will be then! the fiery furnace, and unto all
                those who shall be seized with fear, Thine inescapable judgment-seat.
                Refrain: Let us bless the Father, Son, and Holy Spirit, the Lord!
                I honor God one in Essence, I sing the praises of the three Hypostasis,
                distinct one from another yet not differing in essence, for there is one Godhead
                in the three Hypostases, the Father, the Son and the Holy Spirit.
                Now & Ever ..., From thy most radiant womb, Christ hath come forth as a
                bridegroom from his chamber, and as a great light He hath illumined those in
                darkness. As the Sun of Righteousness he hath shone forth, O pure one,
                enlightening the world.
                Refrain: We praise, bless and worship the Lord, chanting and supremely
                exalting Him throughout all ages.
                Katavasia: Him whom the hosts of heaven glorify, * and before whom
                tremble the Cherubim and Seraphim, * let every breath and all creation *
                praise, bless, and supremely exalt, * throughout all ages.
                And then we chant the Hymn of the Most Holy Theotokos (the Magnificat)
                ODE IX
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Ineffable is the birthgiving of a seedless conception
                Refrain: Have mercy on me, O God, have mercy on me.
                The Lord shall come to punish sinners and to save the righteous. Let us
                weep and lament, and call to mind that day, when our hidden and secret sins will
                be revealed and He will reward each according to what they are due.
                Refrain: Have mercy on me, O God, have mercy on me.
                Moses was filled with fear and trembling when he saw Thy hind parts. How
                then shall I, the wretched one, endure to behold Thy face, when Thou shalt
                come from heaven? But spare me, O compassionate One, by thy merciful gaze.
                Refrain: Have mercy on me, O God, have mercy on me.
                Daniel feared the hour of trial, what then shall I, the wretched one, feel,
                when I come O Lord, to that dreadful day? But grant me before my end to
                worship Thee worthily and to gain Thy Kingdom.
                Refrain: Have mercy on me, O God, have mercy on me.
                The fire is ready, the worm hath prepared itself; yet rejoicing, glory, eternal
                rest, the never-setting light, the gladness of the righteous also await. And who is
                blessed, if not but he who doth escape the former, and inheriteth the later?
                Refrain: Have mercy on me, O God, have mercy on me.
                May I not be rejected from Thy presence O Lord, in Thine anger; may I not
                hear Thy voice casting me off, as one accursed, to the fire. But rather let me
                enter then into the joy of Thine eternal bridal-chamber with Thy saints.
                Refrain: Have mercy on me, O God, have mercy on me.
                My mind hath been wounded, my body hath grown feeble, my spirit hath
                become weak, my speech hath lost its power, and my life hath become deadened,
                the end approacheth. What then shalt thou do, O wretched soul, when the Judge
                cometh to examine thy deeds?
                Glory ..., O Father, single only-Begetter of the only-begotten Son; O only
                Light and Effulgence from the one and only Light; and Thou, one and only Holy
                Spirit from the one God, the Lord from the Lord Who truly is: O Holy Trinity in
                One, save me who doth theologize Thee.
                Now & Ever ..., The marvel of thy childbearing hath filled me with wonder,
                O all-immaculate One. How didst thou conceive without seed Him whom none
                can comprehend? How didst thou remain a Virgin and yet give birth as a
                Mother? Accept with faith that which is above nature, and worship the Child that
                is born: For all that He doth will, He hath the power to do.
                Katavasia: Ineffable is the birthgiving * of a seedless conception, * from a
                mother who knew not a man; * an undefiled childbearing. * For the birth
                of God hath renewed nature, * wherefore all generations rightly worship
                and magnify thee * as the Bride and Mother of God.
            """
            ,'exapostilarion': """
                From the Triodion, in Tone III:
                As I ponder the fearful day of Thy judgment, * and Thine ineffable glory, * I
                am altogether filled with dread, O Lord, * and trembling with fear I cry to Thee:
                * “When Thou comest in glory to earth, * to judge all things O Christ our God, *
                do Thou deliver me from every torment * and deem me worthy, O Master, ** to
                stand at Thy right hand.
                Glory ... Another Exapostilarion from the Triodion
                Behold! the day of the Lord almighty cometh, * and who shall endure the
                fear of His coming? * For it is the day of wrath; * the furnace shall burn, and the
                Judge shall sit and render to each ** the due reward for his works.
                Now & ever ... Theotokion from the Triodion
                As I call to mind the hour of trial and the fearful coming * of the Master the
                Lover of mankind, * I am filled with trembling, and with sad countenance I cry
                unto Thee: * O most righteous Judge, Who alone art plenteous in mercy, ** by
                the intercessions of the Theotokos accept me who repent.
            """
            ,'praises':"""
                from the Triodion, in Tone II:
                I contemplate that day and hour * when we shall all stand naked, like men
                condemned and unclean, before the Judge. * Then shall the trumpet sound and
                the foundations of the earth shall quake, * the dead shall arise from the tombs *
                and all shall be gathered together from every generation. * Then the secrets of all
                shall be made manifest before Thee: * From those who never repented, there
                shall heard be weeping and lamentation, * as they depart to the outer fire; * but
                with gladness and rejoicing the company of the righteous ** shall enter into the
                heavenly bridal chamber.
                How shall it be in that hour on that fearful day, * when the Judge shall sit
                on His dread throne! * The books shall be opened and men’s deeds examined, *
                and those secrets of darkness shall be made public. * Angels shall hasten to and
                fro, gathering all the nations. * Come ye and hearken, kings and princes, slaves
                and free, * sinners and righteous, rich and poor: * for the Judge cometh to pass
                judgment on the whole world. * And who shall bear to stand before His face in
                the presence of the angels * as they call us to give account for our deeds and our
                thoughts, whether by night or by day? * How shall it be then in that hour! * But
                before the end draweth nigh, make haste, O my soul, and cry: ** O God Who
                alone art compassionate, turn me back and save me.
                In Tone VIII: Daniel the prophet, * a man greatly beloved, when he saw the
                power of God, cried aloud: * “The court sat in judgment, and the books were
                opened.” * Consider well, my soul: dost thou fast? * Then despise not thy
                neighbor. * Dost thou abstain from food? * Condemn not thy brother, lest thou
                be sent away into the fire, there to burn as wax. ** But may Christ lead thee
                without stumbling into His Kingdom.
                In Tone I: Let us cleanse ourselves, brethren, * with the Queen of the
                virtues: * for behold, she cometh, bringing unto us a wealth of blessings. * She
                quelleth the uprising of the passions, * and reconcileth those that have sinned to
                the Master. * Therefore let us welcome her with gladness, and cry aloud to Christ
                our God: * O Thou Who didst rise from the dead, ** keep us uncondemned as
                we render glory unto Thee, Who alone art sinless.
                Glory ..., in Tone I:
                Let us cleanse ourselves, brethren, * with the Queen of the virtues: * for
                behold, she cometh, bringing unto us a wealth of blessings. * She quelleth the
                uprising of the passions, * and reconcileth those that have sinned to the Master.
                * Therefore let us welcome her with gladness, and cry aloud to Christ our God: *
                O Thou Who didst rise from the dead, ** keep us uncondemned as we render
                glory unto Thee, Who alone art sinless.
                Now & ever ..., in Tone II:
                Most Blessed art Thou, O Virgin Theotokos, * for through Him Who
                became incarnate of thee is Hades led captive, * Adam recalled, the curse
                annulled, Eve set free, death slain, * and we are given life. Wherefore, we cry
                aloud in praise: * Blessed art Thou, O Christ God, * Who hast been thus wellpleased, glory to Thee.
            """
        } #Matins
        ,'liturgy': {
            'beatitudes': [
                """
                    At Thy fearful coming, O Christ, when Thou shall appear from heaven and
                    set up the thrones, and the books shall be opened, then spare, O Savior, spare
                    Thy creature.
                """
                ,"""
                    Since God is the Judge, nothing can help thee there, no zeal, no skill, no
                    glory, no friendship, but only the strength that thou hast gained, O my soul, from
                    thy works.
                """
                ,"""
                    Glory ..., I sing the praises of the Triune Godhead, the Father, Son and
                    divine Spirit, one sovereign Principle divided in three Hypostases.
                """
                ,"""
                    Now & Ever ..., Thou art the gate through which God alone hath passed,
                    entering in and coming out, yet not breaking the seal of thy virginity O pure one:
                    Jesus, the Creator of Adam, and thy Son.
                """
            ]
            ,'kontakion': """
                Kontakion from the Triodion, in Tone I:
                Now & ever ..., When Thou comest, O God, upon the earth with glory, *
                the whole world will tremble. * The river of fire will flow before Thy judgment
                seat, * the books shall be opened and secrets revealed. * Deliver me then, from
                the unquenchable fire, ** and count me worthy to stand on Thy right hand, O
                Judge most righteous.
            """
            ,'prokeimenon':"""
                Prokeimenon from the Triodion, in Tone III: Great is our Lord, and
                great is His strength; * and of His understanding there is no measure.
                Verse: Praise ye the Lord, for a psalm is a good thing: let praise be
                sweet unto our God.
            """
            ,'readings': """
                1ST EPISTLE TO THE CORINTHIANS: (I COR 8:8-9:2)
                Brethren: Meat commendeth us not to God: for neither, if we eat, are we
                the better; neither, if we eat not, are we the worse. But take heed lest by any
                means this liberty of yours become a stumbling-block to them that are weak. For
                if any man see thee which hast knowledge sit at meat in the idol’s temple, shall
                not the conscience of him which is weak be emboldened to eat those things
                which are offered to idols; And through thy knowledge shall the weak brother
                perish, for whom Christ died? But when ye sin so against the brethren, and
                wound their weak conscience, ye sin against Christ. Wherefore, if meat make my
                brother to offend, I will eat no flesh while the world standeth, lest I make my
                brother to offend. Am I not an apostle? am I not free? have I not seen Jesus
                Christ our Lord? are not ye my work in the Lord? If I be not an apostle unto
                others, yet doubtless I am to you: for the seal of mine apostleship are ye in the
                Lord.
                Alleluia from the Triodion, in Tone VIII:
                Verse: Come, let us rejoice in the Lord. Let us shout with jubilation
                unto God our Savior.
                Verse: Let us come before His countenance with thanksgiving, and with
                Psalms let us shout in jubilation unto Him.
                GOSPEL ACCORDING TO ST. MATHEW (25:31-46)
                The Lord said: When the Son of man shall come in his glory, and all the
                holy angels with him, then shall he sit upon the throne of his glory: And before
                him shall be gathered all nations: and he shall separate them one from another, as
                a shepherd divideth his sheep from the goats: And he shall set the sheep on his
                right hand, but the goats on the left. Then shall the King say unto them on his
                right hand, Come, ye blessed of my Father, inherit the kingdom prepared for you
                from the foundation of the world: For I was an hungred, and ye gave me meat: I
                was thirsty, and ye gave me drink: I was a stranger, and ye took me in: Naked,
                and ye clothed me: I was sick, and ye visited me: I was in prison, and ye came
                unto me. Then shall the righteous answer him, saying, Lord, when saw we thee
                an hungred, and fed thee? or thirsty, and gave thee drink? When saw we thee a
                stranger, and took thee in? or naked, and clothed thee? Or when saw we thee
                sick, or in prison, and came unto thee? And the King shall answer and say unto
                them, Verily I say unto you, Inasmuch as ye have done it unto one of the least of
                these my brethren, ye have done it unto me. Then shall he say also unto them on
                the left hand, Depart from me, ye cursed, into everlasting fire, prepared for the
                devil and his angels: For I was an hungred, and ye gave me no meat: I was thirsty,
                and ye gave me no drink: I was a stranger, and ye took me not in: naked, and ye
                clothed me not: sick, and in prison, and ye visited me not. Then shall they also
                answer him, saying, Lord, when saw we thee an hungred, or athirst, or a stranger,
                or naked, or sick, or in prison, and did not minister unto thee? Then shall he
                answer them, saying, Verily I say unto you, Inasmuch as ye did it not to one of
                the least of these, ye did it not to me. And these shall go away into everlasting
                punishment: but the righteous into life eternal.
                Communion Verse: Praise ye the name of the Lord in the heavens,
                praise him in the highest:
                Communion Verse: Rejoice in the Lord, O ye righteous; praise is meet
                for the upright. Alleluia, Alleluia, Alleluia
            """
        } #Liturgy
    } #Service
    ,'-49': { #Cheesefare Sunday
        'vespers': {
            'stichera_tone': 'in Tone VI:'
            ,'stichera': [
                """
                    The Lord my Creator took me as dust from the earth * and formed me into
                    a living creature, * breathing into me the breath of life; * He honored me, setting
                    me as ruler upon the earth over all things visible, * and making me a companion
                    of the angels. * But Satan the deceiver, using the serpent as his instrument, * by
                    means of food seduced me; * separating me from the glory of God * and gave
                    me over to the earth and to the lowest depths of death. ** But, O Master, as
                    Thou art compassionate, call me back again.
                """
                ,"""
                    I, the wretched one, have cast off the robe woven by God, * and by the
                    counsel of the enemy have disobeyed Thy divine command, * O Lord, I am
                    clothed now in fig leaves and in garments of skin, * condemned to eat the bread
                    of toil, * The earth hath been cursed, bearing thorns and thistles for me. * But,
                    do Thou Who in the last times * wast made flesh of the Virgin, * call me back
                    again ** and bring me into Paradise.
                """
                ,"""
                    O all-precious Paradise, unsurpassed in goodness, * the tabernacle built by
                    God, * unending gladness and delight, the glory of the righteous, * the beauty of
                    the prophets, * and dwelling-place of the saints, * with the sound of thy rustling
                    leaves pray to the Creator of all: * That He open unto me * the gates which I
                    have closed by my transgression, * and that He may deem me worthy to partake
                    of the Tree of Life ** and of the joy which before I delighted in, when in thee.
                """
                ,"""
                    Adam was banished from Paradise through disobedience * and cast out
                    from delight, * beguiled by the words of a woman. * Naked he sat outside the
                    garden, lamenting * “Woe is me!” * Wherefore let us all make haste to accept the
                    season of the Fast * and hearken to the teachings of the Gospel, * that by them
                    we may gain Christ’s mercy ** and receive once more a dwelling-place in
                    Paradise.
                """
            ]
            ,'doxastichon': """
                Adam sat before Paradise * and, lamenting his nakedness, he wept: * “Woe
                is me! By evil persuasion I have been deceived and led astray, * and am now
                exiled from glory. * Woe is me! * lacking noetic insight I am now naked, and in
                need. * O Paradise, no more shall I take pleasure in thy joys; * no more shall I
                look upon the Lord my God and Maker, * for I shall return to the earth from
                whence I was taken. * O merciful and compassionate Lord, I cry unto Thee: **
                Have mercy on me who have fallen.”
            """
            ,'aposticha_theotokion': """
                Glory from the Triodion ..., in Tone VI:
                Adam was cast out of Paradise through eating. * Seated before the gates he
                wept, * lamenting with a compunctionate voice and saying: * “Woe is me, what
                have I suffered wretched as I am! * I transgressed one commandment of the
                Master, * and now I am deprived of every blessing. * O most holy Paradise,
                planted for my sake and shut because of Eve, * pray to Him that created thee
                and fashioned me, * that once more I may take pleasure in thy flowers.” * Upon
                which the Savior said unto him: * “I desire not the loss of the creature which I
                have fashioned, * but desire that he should be saved and come to the knowledge
                of the truth; ** and when he doth come to me I will not cast him out.”
                Now & Ever ..., in Tone VI:
                Christ the Lord, my Creator and Redeemer, * Who came forth from thy
                womb, O most pure one, * and clothed Himself in my nature, * hath freed Adam
                from the primal curse. * Wherefore, like the angel * we unceasingly cry out to
                thee, O all-pure one, * who art truly the Mother of God and Virgin: * Rejoice!, O
                Sovereign Lady, ** the intercession, protection and salvation for our souls!
            """
        } #Vespers
        ,'matins': {
            'after50': """
                in Tone VIII:
                Glory ..., The gates of repentance, do Thou open unto me, O Giver of Life,
                * for early in the morning my spirit seeketh Thy holy temple, * bearing the
                temple of my body all defiled. * But as One who art compassionate * cleanse it
                by Thy loving-kindness and mercy.
                Now & ever ..., Guide me on the paths of salvation, O Theotokos: * for I
                have polluted my soul with shameful deeds * and wasted all my life in
                slothfulness. * but by thine intercessions * do thou deliver me from all impurity.
                In Tone VI:
                Have mercy upon me, O God, * according to Thy great mercy: * and
                according to the multitude of Thy compassion * blot out my transgressions.
                In Tone VIII: As I the wretched one ponder the multitude of evil deeds I
                have done, * I tremble for fear of the dread day of judgment. * But trusting in
                Thy compassionate mercy, * like David do I cry unto Thee: * “Have mercy upon
                me, O God, according to Thy great mercy”.
            """
            ,'canon': """
                ODE I
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmoc: When Israel walked on foot in the sea ...
                Refrain: Have mercy on me, O God, have mercy on me.
                Come, O wretched soul, and weep today over thine acts, remembering how
                once thou was stripped naked in Eden and cast out from delight and unending
                joy.
                Refrain: Have mercy on me, O God, have mercy on me.
                In Thine abundant compassion and mercy, O Fashioner of creation and
                Maker of all, Thou hast taken me from the dust and given me life, commanding
                me to sing Thy praises with Thine angels.
                Refrain: Have mercy on me, O God, have mercy on me.
                For the sake of the wealth of Thy goodness, O Creator and Lord, Thou
                didst plant the sweetness of Paradise in Eden, bidding me to take delight of the
                fair and pleasing, and never-ending fruits therein.
                Glory ..., Woe to thee, O my wretched soul! Thou hast received authority
                from God to take thy pleasure in the joys of Eden, but He commanded thee to
                not eat the fruit of knowledge. Why then hast thou transgressed the law of God?
                Now & Ever ..., O Virgin Birthgiver of God, as a daughter of Adam by
                birth, and a Parent of Christ God by grace, do thou call me who am banished
                from Eden.
                Katavasia: When Israel walked on foot in the sea as on dry land, * on
                seeing their pursuer Pharaoh drowned, * they cried: * Let us sing to God *
                a song of victory.
                ODE III
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmoc: There is none as holy as Thee, ...
                Refrain: Have mercy on me, O God, have mercy on me.
                The crafty serpent long ago envied my honor and whispered deceit into
                Eve’s ear. Woe is me! for by her I was led astray and banished from the banquet
                of life.
                Refrain: Have mercy on me, O God, have mercy on me.
                Foolishly I stretched out my hand and tasted of the tree of knowledge, from
                which God hath commanded me to in no-wise eat; and I was bitterly cast out
                from divine glory.
                Glory ..., Woe to thee, O my wretched soul! How hast thou not recognized
                the deception of the enemy? How hast thou not perceived his deceit and envy?
                For thou art now darkened in mind having transgressed the commandments of
                thy Creator.
                Now & Ever ..., Thou art my hope and protection O pure One, for by thy
                childbearing thou alone hast covered the ancient fall of Adam, clothing me once
                again with incorruption.
                Katavasia: There is none as holy as Thou, * O Lord my God, * who hast
                exalted the horn of The faithful O good One, * and strengthened us upon
                the rock * of Thy confession.
                Sessional Hymns from the Triodion, in Tone IV:
                Adam was cast out from the delight of Paradise: * eating the bitter food and
                lacking self-constraint, * keeping not the Master’s commandment, * and was
                thereby condemned to work the earth from which he had himself been taken, *
                eating his bread in toil. * Wherefore let us love abstinence, * that we not weep as
                he did outside the gates of Paradise, ** but by it may we enter therein.
                Glory ..., in Tone IV:
                The season of the virtues hath now appeared, * and the judge is at the door.
                * Let us not be of a sullen countenance, * let us keep the Fast, offering tears,
                contrition and almsgiving; * and let us cry aloud: * We have sinned more than
                there are grains of sand in the sea; * but, do Thou O Redeemer of mankind, **
                forgive each of us, that we may receive a crown of incorruption.
                Now & Ever ..., in Tone IV:
                We shall never, O Theotokos, * keep silent nor cease, unworthy though we
                be, * to praise thy power. * For had we not the protection of thine intercessions,
                * who would have delivered us from so many dangers? * Who would have
                preserved us free till now? * We shall never forsake thee, O lady, ** for thou dost
                always save thy servants from every misfortune.
                ODE IV
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmoc: Christ is my power ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I, the wretched one, was deemed worthy of honor from Thee O Master in
                Eden. But alas! I have been deceived by the envy of the devil and cast out from
                before Thy face!
                Refrain: Have mercy on me, O God, have mercy on me.
                Weep for me, O ye ranks of angels, beauty of Paradise and glory of the
                garden: for in my misery I have been led astray and rebelled against God.
                Refrain: Have mercy on me, O God, have mercy on me.
                O thou blessed meadow, ye gardens planted by God, thou sweetness of
                Paradise: let your leaves, like eyes, shed tears on my behalf, for I am naked and a
                stranger to God’s glory.
                Glory ..., No longer do I see thee, nor delight in thy splendor and divine
                radiance, O precious Paradise. For having angered my Creator, I am naked and
                have been driven out into the world.
                Now & Ever ..., O most holy Lady, open unto all the faithful the gates of
                paradise, as once they were shut by the transgression of Adam, and open to me
                the gates of thy mercy.
                Katavasia: Christ is my power, * my God and my Lord, * the holy Church
                divinely singeth, * crying with a pure mind, * keeping festival in the Lord.
                ODE V
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmoc: Illumine with Thy divine light, I pray, O Good One ...
                Refrain: Have mercy on me, O God, have mercy on me.
                Of old, the enemy who hateth mankind, envied the life of happiness that I
                had in Paradise, and taking the form of a serpent caused me to stumble, thereby
                showing me to be a stranger to eternal glory.
                Refrain: Have mercy on me, O God, have mercy on me.
                I weep and lament in soul, and with mine eyes I shed abundant tears, when I
                reflect upon, and understand my nakedness, which I have gained from
                transgressing.
                Glory ..., From the earth I was fashioned by the hand of God, and I, the
                wretched one, was told that to the earth I shall return again. Who will not weep
                for me, who am cast out from God’s presence, exchanging Eden for Hades.
                Now & Ever ..., We the faithful proclaim thee to be the mystical bridalchamber of glory, O all-immaculate Birthgiver of God. Wherefore I entreat thee
                O pure One: Raise me up, for I am fallen, and make me a dweller in the bridalchamber of Paradise.
                Katavasia: Illumine with Thy divine light, I pray, O Good One, * the souls
                of those who with love rise early to pray to Thee, * that they may know
                Thee, O Word of God, * as the true God, * Who recalleth us from the
                darkness of sin.
                ODE VI
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmoc: Beholding the sea of life ...
                Refrain: Have mercy on me, O God, have mercy on me.
                In Eden Thou didst clothe me with a divinely woven garment O
                compassionate Savior; but I, the wretched one, having believed the deceiver,
                have neglected Thy commandment and find myself naked.
                Refrain: Have mercy on me, O God, have mercy on me.
                O my most wretched soul, through thy carelessness thou hast departed far
                from God; and depriving thyself of the delight of Paradise, thou hast been
                separated from the angels, and led down into corruption. O How thou art fallen!
                Glory ..., O almighty God, have mercy and take pity on the works of Thy
                hands. I pray Thee O good One, turn not away from me, who hath cut himself
                off from the choir of Thine angels.
                Now & Ever ..., O Mary chosen by God, Queen of all, thou didst give birth
                to the Lord, Redeemer and King of all, whereas I am a prisoner and an exile
                from Paradise: do thou call me back.
                Katavasia: Beholding the sea of life surging with the tempest of
                temptations, * I run to Thy calm haven, and cry to Thee: * Raise up my
                life from corruption, * O Most Merciful One.
                Kontakion from the Triodion, in Tone VI:
                O Master, Guide to wisdom, * Giver of prudent counsel, * Instructor of the
                foolish and Champion of the poor, * establish, and enlighten my heart. * Grant
                unto me thy word, O Word of the Father, * for behold! I shall not stop my lips *
                from crying out to Thee: ** “I am fallen, O compassionate One have mercy on
                me”.
                Ikos: Banished from the delights of Paradise, Adam sat outside and wept,
                and beating his hands upon his face he said: “I am fallen, in Thy compassion
                have mercy on me.” When Adam saw the angel drive him out and shut the door
                of the divine garden, he groaned aloud and said: “I am fallen, in Thy compassion
                have mercy on me.” O Paradise, share in the sorrow of thy master who hath
                been brought to poverty, and with the rustling of thy leaves beseech the Creator
                that He not keep thy gate closed. O compassionate One have mercy on me who
                am fallen. O Paradise, all-perfect, all-holy and most rich, planted for Adam’s sake
                and shut because of Eve, beseech God on behalf of the fallen. O compassionate
                One have mercy on me who am fallen.
                SYNAXARION READING
                Verse: Let all the earth weep bitterly, with the fathers of our race.
                Verse: For it is fallen with those who tasted The sweet fruit of the tree.
                On this day we commemorate the fall of Adam the first-formed from
                partaking of the fruit of Paradise, which our holy and divine Fathers have
                appointed for the Sunday before Great Lent in order to demonstrate the great
                healing effect of the fast upon human nature and the great harm of intemperance
                and disobedience. Setting aside the countless instances of these vices in the
                world, the Fathers have put forth a vivid example in first-formed Adam, who
                suffered great harm in his total failure to fast and brought this harm upon our
                nature. He did not keep the first commandment of a beneficial fast which God
                had required of mankind, but yielding to the desires of his belly and of the
                serpent through Eve, he not only did not become godlike, but he gave rise to
                death, bringing perdition upon all our race. For the sake of Adam’s intemperance
                the Lord fasted for forty days and was obedient. It was for this reason that the
                holy Apostles conceived this present forty-day fast, so that as Adam forfeited
                incorruption through his intemperance, we may regain it through abstinence.
                Also, as was stated earlier, it was the intent of the Holy Fathers through the
                Triodion to relate in a condensed form all of God’s acts from the beginning to
                the end of the world. Since Adam’s transgression and fall through the eating of
                the fruit of the tree is the principal cause of the state of mankind, the Fathers
                exhort us who are observing this commemoration to avoid Adam’s sin and to
                shun intemperance in all things. Now it was on the sixth day that Adam was
                created by the hand of God after His own image and through His life-giving
                breath. Receiving God’s commandment, he lived in Paradise up until the sixth
                hour, when he disobeyed God’s command and was driven out. And as he
                stretched out his hand at the sixth hour to touch the fruit, so the new Adam,
                Christ, at the sixth day and hour stretched out his hands upon the Cross,
                annulling the sentence of perdition brought about by the former Adam. For he
                was created in the midst of corruption and incorruption through providence with
                the freedom of choice. God could have made Adam sinless, yet His providence
                was to provide for reparation. For this cause He gave His commandment that
                Adam might partake of all in the garden, save the one tree. Does this not mean
                that Adam was meant to understand the essence of all created by the divine
                power, but was not to attempt to understand the essence of the Godhead; That
                is to say God commanded Adam to concern himself will all other elements and
                qualities, reasoning with his mind to the glory of God; for this is true
                nourishment. But he was not to search for the divine essence: God, who He is,
                where He is and how He brought all things into being out of nothingness. Yet to
                his own harm Adam, having no care for the other things, sought to examine God
                and to determine His essence; and since he was not perfect but still a simple
                child, he failed in his undertaking, when through Eve Satan planted in him the
                desire of becoming Godlike. Some say that the tree of disobedience was a fig
                tree, and becoming aware of their nakedness, Adam and Eve used its leaves to
                cover themselves. For this reason Christ cursed the fig tree as the cause of that
                disobedience, attributing to it a sort of resemblance to sin. For having
                transgressed becoming clothed in mortal flesh and receiving the curse, Adam was
                driven from Paradise. And at God’s command a flaming sword guarded its gates.
                Adam sat before the gates of Paradise and lamented the many blessings he had
                lost in his failure to observe a timely fast. And through him the entire race shared
                in that sentence, until our Creator, taking pity on our nature which because of
                Satan was perishing, was born of the Holy Virgin and lived an exceptional life,
                showing us the path away from the devil, that is abstinence and humility, and
                valiantly gaining the victory over the deceiver, returned us to our former state. In
                their desire to lay all these events before us, the God-bearing fathers have begun
                with the Old Testament: the creation of the world, the fall of Adam through the
                eating of the fruit, which we commemorate today, and later on the words of
                Moses and the prophets and the poetry of David, which impart grace.
                Afterwards in order the events of the New Testament, of which the first is the
                Annunciation, which almost always occurs during Lent through God’s ineffable
                providence, the raising of Lazarus, Palm Sunday, the reading of the sacred
                Gospels during Holy Week, and the profound texts of the holy and saving
                Passion of Christ. After this the Resurrection and the rest up to the descent of
                the Holy Spirit read in the book of Acts, how this event became a proclamation
                that assembled all the saints together, for in the book of Aces the Resurrection is
                confirmed through signs and wonders. Since we have so suffered from Adam’s
                failure to keep the fast, this event is commemorated today at the beginning of
                Great Lent, so that keeping in mind the enormous evil brought about by Adam’s
                intemperance, we may make joyful haste to accept and keep the fast. And as
                Adam sinned in his desire to become godlike, we may thereby receive godliness
                through fasting, tears and humility until God visits us; for without these it is
                impossible to regain that which we have lost. It should be also noted that the
                holy forty-day fast is the tenth part of the entire year. Since out of indolence we
                are not willing to fast constantly or to rid ourselves of evil habits, the Apostles
                and divine Fathers have passed down the Fast to us as a sort of first offering of
                the harvest of our lives. And as we have acted inappropriately for the entire year,
                we may now cleanse our souls through fasting, contrition and humility. We
                should keep the Great Fast with the utmost care. For as there are four seasons in
                the year, so there are four fasts. Yet the divine Apostles have entrusted Lent to
                us as the greatest of the fasts, since it honors the Holy Passion of Christ, His fast
                and His glorification. Moses also fasted forty days before he received the Law,
                also Elijah, Daniel and all who found favor in God’s sight. Adam illustrates for
                us the benefit of the fast as opposed to intemperance. For this reason Adam’s
                banishment from Paradise was appointed by the Holy Fathers to be
                commemorated on this day.
                In Thine ineffable compassion, O Christ our God, make us worthy of the
                nourishment of Paradise, and have mercy on us, as Thou alone lovest mankind.
                Amen.
                ODE VII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmoc: An Angel made the furnace throw dew ...
                Refrain: Have mercy on me, O God, have mercy on me.
                O Lord Who rulest over all the ages, Who by Thine own will created me,
                through the envy of the crafty serpent of old I have been beguiled, and angered
                Thee O Savior: despise me not, O God, but do Thou call me back.
                Refrain: Have mercy on me, O God, have mercy on me.
                Woe is me, in place of wearing a robe of light, I am clothed in a garment of
                shame. I weep from my loss, O Savior, and with faith cry to Thee O good One:
                despise me not, O God, but do Thou call me back.
                Glory ..., The evil serpent in his envy hath wounded all my soul and caused
                me to be banished from the delight of paradise, but O Compassionate Savior:
                despise me not, since Thou art God, and call me back.
                Now & Ever ..., O all-immaculate One, in thy tender compassion accept
                mine entreaty; and grant me forgiveness of mine offenses O pure One, for
                fervently I cry aloud with tears: despise me not, O good One, but do thou call
                me back.
                Katavasia: An Angel made the furnace bedew the holy Children. * But the
                command of God consumed the Chaldeans * and prevailed upon the
                tyrant to cry: * O God of our fathers, Blessed art Thou.
                ODE VIII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmoc: Thou didst make flame sprinkle the Saints with dew ...
                Refrain: Have mercy on me, O God, have mercy on me.
                Of old, Thou didst honor the work of Thy hands with every kind of gift, O
                Lover of mankind,: but, woe to me! the wicked serpent hath deceived us with
                seductive whispering, stripping us of the blessings we had received.
                Refrain: Have mercy on me, O God, have mercy on me.
                Why hast thou hearkened to bitter counsel and disobeyed the divine
                command? Woe to thee, O miserable soul, thou hast grieved God! even though
                thou wast created to ever glorify Him with the angels.
                Refrain: Let us bless the Father, Son, and Holy Spirit, the Lord!
                Thou wast the appointed lord over creeping things and wild beasts: why
                then hast thou conversed with the destroyer of souls? And why hast thou taken
                the deceiver’s counsel as truth?, wretched is thy deception, O my soul!
                Now & Ever ..., O Mary, we hymn thee who art full of the grace of God,
                tabernacle of the Light and dwelling-place of the incarnate God. Wherefore shine
                upon me who am grievously darkened by the passions, the light of mercy, thou
                Hope of the hopeless.
                Refrain: We praise, bless and worship the Lord, chanting and supremely
                exalting Him throughout all ages.
                Katavasia: Thou didst make flame bedew the holy children, * and didst
                burn the sacrifice of a righteous man with water. * For Thou alone, O
                Christ, dost do all as Thou willest, * Thee do we exalt throughout all ages.
                And then we chant the Hymn of the Most Holy Theotokos (the Magnificat)
                ODE IX
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: It is impossible for mankind to see God ...
                Refrain: Have mercy on me, O God, have mercy on me.
                Having taken my fill, and tasted of the fruit of knowledge in Eden, it
                seemed sweet to me, but the end of it was bitter. Woe to thee, wretched soul! See
                how uncontrolled desire hath made thee an exile from Paradise!
                Refrain: Have mercy on me, O God, have mercy on me.
                O God of all, Lord of mercy, look down compassionately upon my humility,
                and cast me not far away from Eden; but may I see the glory from which I have
                fallen, and hasten with lamentations to regain that which I have lost.
                Refrain: Have mercy on me, O God, have mercy on me.
                I lament, I groan and weep, seeing the cherubim with the sword of fire
                guarding the gate of Eden from all transgressors. Woe is me! a transgressor, for I
                cannot enter therein O Savior, unless Thou dost grant it to me.
                Glory ..., I put my trust in the abundance of Thy mercies O Christ Savior,
                and in the Blood from Thy divine side; for through Thy Blood Thou hast
                sanctified the nature of mortal man, O good One, opening unto those that serve
                Thee the gates of Paradise which were formerly closed to Adam.
                Now & Ever ..., O unwedded virgin Theotokos, thou impassable door of
                life, by thy prayers open unto me the locked gates of paradise, that I may glorify
                thee, who after God, art my helper and most powerful refuge.
                Katavasia: It is impossible for mankind to see God * upon Whom the
                orders of Angels dare not gaze; * but through thee, O all-pure one, * did
                the Word Incarnate become a man * and with the Heavenly Hosts * Him
                we magnify and thee we call blessed.
            """
            ,'exapostilarion': """
                Glory ..., The Exapostilarion from the Triodion, in Tone III:
                I, the wretched one O Lord, have disobeyed Thy commandment, * and
                having been stripped of glory, am filled with shame. * Woe is me! who hath been
                banished from the sweetness of Paradise. * O merciful One, have mercy on me
                ** who hath been justly deprived of Thy good things.
                Now & ever ..., Another from the Triodion:
                We were once banished, O Lord, from Paradise, * through eating from the
                Tree; * but Thou hast led us back again, O my God and Savior, * through Thy
                Cross and Passion. * Do Thou strengthen us by these, that we may keep the Fast
                in holiness * and worship Thy divine arising, the Passover of salvation, ** by the
                prayers of her who gave birth to Thee.
            """
            ,'aposticha': """
                from the Triodion, in Tone V:
                Verse: Praise Him with tuneful cymbals, praise Him with cymbals of
                jubilation. * Let every breath praise the Lord.
                “Woe is me” lamented Adam crying aloud: * “For the serpent and the
                woman have deprived me of my boldness before God, * and through eating of
                the tree I have become an exile from the joys of paradise”. * “Woe is me! I can
                no more endure the shame. * From the counsel of the evil-one, * I who was
                once king of all earth’s creatures fashioned by God, * have now become a
                prisoner. * I who was once clothed in the glory of immortality * must now, as a
                mortal, wrap myself miserably in the skin of mortality. * Woe is me! who will
                participate with me in my sorrow? * But, O Lover of mankind, Who hast
                fashioned me from the earth and art clothed in compassion, ** do Thou deliver
                me from the works of the enemy and save me”.
                Verse: I will confess Thee, O Lord, with my whole heart, * I will tell of
                all Thy wonders.
                The arena of the virtues hath been opened, * let all who wish to struggle
                now enter therein, * girding themselves for the noble struggles of the Fast; * for
                those that strive lawfully are justly crowned. * Taking up the armor of the Cross,
                * let us make war against the enemy. * Let us have as our invincible rampart - the
                Faith, * and as our breastplate - prayer, * and as our helmet - almsgiving; * and in
                place of a sword let us make use of fasting * which doth cut away every evil from
                our heart. * If we do this, we shall receive the true crown from Christ the King
                of all, ** at the day of Judgment.
                Verse: I will be glad and rejoice in Thee, * I will chant to Thy name, O
                Most High.
                Tone VI: Adam was driven out of Paradise, * having eaten food as one
                disobedient; * Moses was a God-seer, * because he had cleansed the eyes of his
                soul by fasting. * Wherefore, longing to dwell in Paradise, * let us abstain from all
                needless food; * and if we desire to see God, * let us like Moses fast the forty-day
                fast, with sincere intercessions, patiently praying. * Let us calm the passions of
                our soul, * and subdue the rebelliousness of the flesh. * With light step let us set
                out upon the path to heaven, * where the choirs of angels with never-silent
                voices * hymn the praises of the undivided Trinity, * beholding the unsurpassed
                beauty of the Master. * O Son of God, Giver of Life, in Thee we set our hope: *
                Deem us worthy of a place there with the angelic hosts, * by the intercessions of
                her who bore Thee, O Christ, ** of the apostles and the martyrs and of all the
                venerable saints.
                Verse: Arise, O Lord my God, let Thy hands be lifted high; * forget not
                Thy paupers to the end.
                In Tone VI: The time is now at hand * to start upon the spiritual contest, *
                to gain victory over demonic powers. * to put on the armor of abstinence, * to
                clothe ourselves in the glory of the angels. * to stand with boldness before God.
                * By which things Moses spoke to the Creator, * hearing the voice of the
                invisible One. * By which things also O Lord, * grant that we may worship Thy
                Passion ** and Thy Holy Resurrection, O Lover of mankind.
            """
            ,'aposticha_theotokion': """
                Glory ..., in Tone VI:
                The time is now at hand * to start upon the spiritual contest, * to gain
                victory over demonic powers. * to put on the armor of abstinence, * to clothe
                ourselves in the glory of the angels. * to stand with boldness before God. * By
                which things Moses spoke to the Creator, * hearing the voice of the invisible
                One. * By which things also O Lord, * grant that we may worship Thy Passion
                ** and Thy Holy Resurrection, O Lover of mankind.
                Now & ever ..., in Tone II:
                Most Blessed art Thou, O Virgin Theotokos, * for through Him Who
                became incarnate of thee is Hades led captive, * Adam recalled, the curse
                annulled, Eve set free, death slain, * and we are given life. Wherefore, we cry
                aloud in praise: * Blessed art Thou, O Christ God, * Who hast been thus wellpleased, glory to Thee.
            """
        } #Matins
        ,'liturgy': {
            'beatitudes': [
                """
                    In Eden Thou didst clothe me with a divinely woven garment O
                    compassionate Savior; but I, the wretched one, having believed the deceiver,
                    have neglected Thy commandment and find myself naked.
                """
                ,"""
                    O my most wretched soul, through thy carelessness thou hast departed far
                    from God; and depriving thyself of the delight of Paradise, thou hast been
                    separated from the angels, and led down into corruption. O How thou art fallen!
                """
                ,"""
                    Glory ..., O almighty God, have mercy and take pity on the works of Thy
                    hands. I pray Thee O good One, turn not away from me, who hath cut himself
                    off from the choir of Thine angels.
                """
                ,"""
                    Now & Ever ..., O Mary chosen by God, Queen of all, thou didst give birth
                    to the Lord, Redeemer and King of all, whereas I am a prisoner and an exile
                    from Paradise: do thou call me back.
                """
            ]
            ,'kontakion': """
                in Tone VI
                O Master, Guide to wisdom, * Giver of prudent counsel, * Instructor of the
                foolish and Champion of the poor, * establish, and enlighten my heart. * Grant
                unto me thy word, O Word of the Father, * for behold! I shall not stop my lips *
                from crying out to Thee: ** “I am fallen, O compassionate One have mercy on
                me”.
            """
            ,'prokeimenon':"""
                Prokeimenon for in Tone VIII: Make your vows * and pay them to the
                Lord our God.
                Verse: In Judea is God known; His name is great in Israel.
            """
            ,'readings': """
                EPISTLE TO THE ROMANS (13:11B - 14:4)
                Brethren: know ye that now it is high time to awake out of sleep: for now is
                our salvation nearer than when we believed. The night is far spent, the day is at
                hand: let us therefore cast off the works of darkness, and let us put on the armor
                of light. Let us walk honestly, as in the day; not in rioting and drunkenness, not
                in chambering and wantonness, not in strife and envying. But put ye on the Lord
                Jesus Christ, and make not provision for the flesh, to fulfill the lusts thereof.
                Him that is weak in the faith receive ye, but not to doubtful disputations. For
                one believeth that he may eat all things: another, who is weak, eateth herbs. Let
                not him that eateth despise him that eateth not; and let not him which eateth not
                judge him that eateth: for God hath received him. Who art thou that judgest
                another man’s servant? to his own master he standeth or falleth. Yea, he shall be
                holden up: for God is able to make him stand.
                Alleluia from the Triodion, in Tone VI:
                Verse 1: It is good to give praise unto the Lord, and to chant unto Thy
                Name, O Most High.
                Verse 2: To proclaim in the morning Thy mercy, and Thy truth by
                night.
                GOSPEL ACCORDING TO ST. MATTEW (6:14-21)
                The Lord said: if ye forgive men their trespasses, your heavenly Father will
                also forgive you: But if ye forgive not men their trespasses, neither will your
                Father forgive your trespasses. Moreover when ye fast, be not, as the hypocrites,
                of a sad countenance: for they disfigure their faces, that they may appear unto
                men to fast. Verily I say unto you, They have their reward. But thou, when thou
                fastest, anoint thine head, and wash thy face; That thou appear not unto men to
                fast, but unto thy Father which is in secret: and thy Father, which seeth in secret,
                shall reward thee openly. Lay not up for yourselves treasures upon earth, where
                moth and rust doth corrupt, and where thieves break through and steal: But lay
                up for yourselves treasures in heaven, where neither moth nor rust doth corrupt,
                and where thieves do not break through nor steal: For where your treasure is,
                there will your heart be also.
            """
        } #Liturgy
    } #Service
    ,'-42': { #1st Sunday | Sunday of Orthodoxy
        'vespers': {
            'stichera_tone': 'in Tone VI:'
            ,'stichera': [
                """
                    Inspired by Thy Spirit, O Lord * the prophets foretold that Thou, Whom
                    nothing can contain, * and Who hast shone forth in eternity before the morning
                    star * from the immaterial and bodiless womb of the Father, * wast to become a
                    child, taking flesh from the Virgin, * being joined to mankind and seen by those
                    on earth. * Through them O Compassionate One * count as worthy of Thy light,
                    * those who ceaselessly sing ** the praises of Thine ineffable and holy
                    Resurrection.
                """
                ,"""
                    Having preached Thee in word, * the divinely-inspired prophets, honoring
                    Thee in works, * received as their reward unending life. * For they refused, O
                    Master, * to worship the creation instead of Thee, the Creator, * renouncing the
                    whole world * for the sake of the Gospel, * they were conformed in their
                    suffering, to Thy Passion * which they had foretold. * By their intercessions,
                    count us worthy * to pass without offense through the period of the Fast, ** for
                    Thou alone art plenteous in mercy.
                """
                ,"""
                    Thou Who art uncircumscribed in Thy divine nature, * wast pleased in the
                    last times O Lord, to take flesh and become circumscribed; * and in assuming
                    flesh, * Thou hast also taken upon Thyself all its distinctive characteristics. *
                    Therefore we depict the likeness of Thy countenance, * venerating it with honor,
                    * we are exalted to the love of Thee, * and from it we receive the grace of
                    healing, ** thus following the holy traditions of the apostles.
                """
                ,"""
                    As a precious adornment * the Church of Christ hath received the venerable
                    and holy icons * of the Savior Christ, * of the Mother of God, and of all the
                    saints. * Celebrating now their triumphant restoration, * she is made bright and
                    splendid with grace, * rejecting and driving away indolent imaginings of the
                    heretics, * with great rejoicing she giveth glory unto God the Lover of mankind,
                    ** Who for her sake endured His voluntary Passion.
                """
            ]
            ,'doxastichon': """
                from the Triodion, in Tone II:
                The grace of truth hath shone forth upon us; * the mysteries darkly
                prefigured in times past have now been openly fulfilled. * For behold, the
                Church is clothed in the unsurpassed beauty * of the icons of the incarnate
                Christ * which was foreshadowed by the ark of testimony. * This is the
                upholding of the Orthodox faith; * for if we uphold the icon of the Savior,
                Whom we worship, * we shall not go astray. * Let all those who do not confess
                this faith be covered with shame; * but we shall glory in venerating the icon of
                the Word made flesh, * which we worship not as an idol. * So let us kiss it, and
                with all the faithful cry aloud: ** O God, save Thy people and bless Thine
                inheritance.
            """
            ,'aposticha_theotokion': """
                Glory from the Triodion..., in Tone II:
                Advancing from ungodliness to honorable faith, * and illumined with the
                light of knowledge, * let us clap our hands and with psalmody, * offer praise and
                thanksgiving unto God; * and with honor let us venerate the holy icons of Christ,
                * of the most pure Virgin and all the saints, * whether depicted on walls, on
                wooden panels or on holy vessels, * rejecting the impious faith of the heterodox.
                * For, as Basil says, the honor given the icon * passeth through to the prototype
                represented by it. * By the prayers of Thine all-immaculate Mother, O Christ
                God * and of all the saints, ** we beseech Thee, to bestow upon us Thy great
                mercy.
                Now & ever ..., Theotokion, in Tone II:
                O new wonder greater than all the wonders of old! * For who hath ever
                known a mother to give birth without having known a man, * and to bear on her
                arm Him Who sustaineth all creation? * Yet it was the will of God to be born. *
                O most pure one, who carried Him as an infant in Thine embrace * and before
                Whom thou hast a mother’s boldness: * cease not to pray on behalf of those
                who honor thee, ** that He have compassion and save our souls.
            """
        } #Vespers
        ,'matins': {
            'troparion': """
                Glory ..., the Troparion of the Sunday of Orthodoxy, in Tone II:
                We venerate Thine immaculate icon, O good One, * asking the pardon of our
                transgressions, O Christ God. * For of Thine own will Thou wast well-pleased to
                ascend the Cross in the flesh, * that Thou mightest deliver from the slavery to
                the enemy those Whom Thou hast fashioned. * Therefore in thanksgiving we cry
                to Thee: * Thou didst fill all things with joy, O our Savior, ** when Thou camest
                to save the world.
                Now & ever ..., Theotokion, in Tone II:
                All of thy most glorious mysteries are beyond comprehension, * O
                Theotokos; * for, thy purity sealed and thy virginity intact, * thou art known to
                be a true Mother, having given birth unto God. ** Him do thou entreat, that our
                souls be saved.
            """
            ,'after50': """
                in Tone VIII:
                Glory ..., The gates of repentance, do Thou open unto me, O Giver of Life,
                * for early in the morning my spirit seeketh Thy holy temple, * bearing the
                temple of my body all defiled. * But as One who art compassionate * cleanse it
                by Thy loving-kindness and mercy.
                Now & ever ..., Guide me on the paths of salvation, O Theotokos: * for I
                have polluted my soul with shameful deeds * and wasted all my life in
                slothfulness. * but by thine intercessions * do thou deliver me from all impurity.
                In Tone VI:
                Have mercy upon me, O God, * according to Thy great mercy: * and
                according to the multitude of Thy compassion * blot out my transgressions.
                In Tone VIII: As I the wretched one ponder the multitude of evil deeds I
                have done, * I tremble for fear of the dread day of judgment. * But trusting in
                Thy compassionate mercy, * like David do I cry unto Thee: * “Have mercy upon
                me, O God, according to Thy great mercy”.
            """
            ,'canon': """
                ODE I
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Through the deep of the Red Sea ...,
                Refrain: Glory to Thee our God, glory to Thee.
                Leaping up with joy, let us the faithful cry aloud today: How marvelous are
                Thy works, O Christ! How great is Thy might! For Thou hast made us of one
                mind and brought about concord.
                Refrain: Glory to Thee our God, glory to Thee.
                O Godly-wise people, come let us celebrate a day of joy; for heaven and earth
                now rejoiceth, with all the hosts of angels and all mankind, each making festival.
                Refrain: Glory to Thee our God, glory to Thee.
                Seeing this great blessing we have received, let us clap our hands; for the
                divided members of Christ have been brought together, and we give praise to
                God Who hath bestowed peace.
                Glory ..., Today a festival of victory hath been granted to the Church,
                through the divinely-inspired intent and council of Michael and Theodora, who
                piously uphold the faith of our Sovereigns.
                Now & Ever ..., The swords of impious heresies have failed: For in deep
                reverence, O all-immaculate pure One, gazing now upon thy temple, beauteously
                adorned with icons, we rejoice with a most holy joy.
                Katavasia: Through the deep of the Red Sea, * marched dry shod Israel of
                old, * and by Moses’ outstretched hands, * raised in the form of a cross, *
                the power of Amalek was routed in the wilderness.
                ODE III
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Thy Church, O Christ ...,
                Refrain: Glory to Thee our God, glory to Thee.
                No longer now are the impious heretics exalted in their pride: For the power
                of God hath firmly established Orthodoxy.
                Refrain: Glory to Thee our God, glory to Thee.
                Let the prophets sprinkle upon us today the life-giving dew from heaven, at
                the restoration of the faith
                Refrain: Glory to Thee our God, glory to Thee.
                In Godly harmony, let the mystical trumpets of Christ’s apostles sound forth,
                proclaiming the re-establishment of the precious icons.
                Glory ..., Let us sing in praise of Christ, Who hath appointed a devout and
                pious Empress to rule over us, together with her heir, crowned by God.
                Now & Ever ..., Shine now upon the faithful who have gathered in thy holy
                house, O most pure One, the light of grace, we pray thee.
                Katavasia: Thy Church, O Christ, rejoiceth in Thee crying aloud: * Thou,
                O Lord, art my strength, * my refuge and foundation.
                Sessional Hymn from the Triodion, in Tone I:
                Depicting Thy divine form in icons, O Christ, * we openly proclaim Thy
                birth, * Thine ineffable miracles and Thy voluntary Crucifixion. * From whence
                devils are driven out in fear ** and their fellow-workers - the heretics, lament in
                shame.
                Glory ..., The divine and beauteous images of the prophets, * of the apostles
                the holy martyrs, and of all the saints * are rendered in holy icons; * in which
                Thou, the unwedded Bride, * art also rendered beauteously with noetic splendor,
                * O Mother of Zion on high.
                Now & Ever ..., With love, O honored Virgin, we venerate thy holy icon;
                with one accord we proclaim thee to be the true Mother of God, and in faith we
                bow down before thee. Since thou hast power to do all things, be our guardian
                and our strong protection, and drive far from us every tribulation.
                ODE IV
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Seeing Thee, the Sun of righteousness ...
                Refrain: Glory to Thee our God, glory to Thee.
                Through the divine descent of the Comforter sanctify Thy temple, and by
                His coming banish the delusion of heresy, O plenteously merciful Word of God.
                Refrain: Glory to Thee our God, glory to Thee.
                Deliver Thy people from the aggression of the impious, and enkindle within
                them a zeal for piety, as they cry aloud to Thee in faith: Glory to Thy power, O
                Lord.
                Refrain: Glory to Thee our God, glory to Thee.
                Seeing the churches of God radiant with the sacred depictions and images of
                Christ and the Theotokos, we rejoice with a holy joy.
                Glory ..., Adorned with her royal crown, the Empress, out of a true love for
                the Kingdom of Christ, hath restored in all the churches His most pure icon and
                the images of the saints.
                Now & Ever ..., Thou didst bear the Divine Word incarnate, O divinely
                glorious One, revealed as one full of grace, wherefore we consecrate thy bright
                and splendid temple.
                Katavasia: Beholding Thee, the Sun of righteousness, * lifted up upon
                the cross, * the Church now standeth arrayed and doth worthily cry
                aloud: * Glory be to Thy power, O Lord!
                ODE V
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Thou, O Lord, who camest into the world ...,
                Refrain: Glory to Thee our God, glory to Thee.
                Firmly establish Thy church, O Lord, that unto the ages of ages she may
                stand unshaken by the tempest of heresy.
                Refrain: Glory to Thee our God, glory to Thee.
                O Thou Who alone art good and the source of goodness, raise up the horn
                of the Orthodox who honor Thine image.
                Glory ...,The never-setting light of piety hath shone forth upon us, by the
                divinely-inspired commandment of our faithful pastors.
                Now & Ever ..., Renew for us the ancient splendors, O most pure Mother of
                God, and sanctify this thy dwelling with thy grace.
                Katavasia: Thou, O Lord, who camest into the world, * art my light, * a
                holy light turning from the darkness of ignorance * those who sing Thy
                praises in faith.
                ODE VI
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: The church crieth out unto Thee ...
                Refrain: Glory to Thee our God, glory to Thee.
                The Master’s countenance is depicted, honored with faith, and venerated;
                whereby the Church regaineth her boldness before God, reverently glorifying the
                Savior.
                Refrain: Glory to Thee our God, glory to Thee.
                The Church of Christ hath been delivered from the darkness of heresy:
                putting on a robe of gladness, she is clothed in the light of divine grace.
                Glory ..., The Orthodox people have regained the light and glory which it had
                of old, through the decree of the Empress Theodora and her pious son the
                Emperor Michael.
                Now & Ever ..., He Who of old commanded Moses to make the ark of the
                covenant, came to dwell within thee, as if in a noetic ark: He alone is supremely
                glorified, making thy temple glorious with miracles.
                Katavasia: The church crieth out unto Thee O Lord, * “I will sacrifice
                unto Thee with a voice of praise” * having been cleansed of the blood of
                the demons’ * by the blood that for mercy’s sake flowed from Thy side.
                Kontakion from the Triodion, in Tone VIII:
                The uncircumscribed Word of the Father hath become circumscribed, *
                taking flesh from thee, O Theotokos, * and He hath restored the sullied image to
                its ancient glory, filling it with divine beauty. ** This our salvation we confess in
                deed and word, and we depict it in the holy icons.
                Ikos: Enlightened by this mystery of God’s providence, the divinely-inspired
                prophets foretold it of old; and this they did for our sakes, who see the
                fulfillment of the ages. Receiving through this mystery divine knowledge, we
                know one Lord and God, glorified in three Hypostases, and Him alone do we
                worship; we have one faith, one baptism, and clothed in Christ, we confess in
                deed and word our salvation, depicting it in the holy icons.
                SYNAXARION
                Verse: I rejoice when I see the veneration due the icons,
                Verse: Once so ignominiously rejected.
                On this first Sunday of Great Lent, the Sunday of Orthodoxy, the Church of
                Christ celebrates the restoration of the holy and venerable icons by the Emperor
                Michael, the holy and blessed Empress Theodora and the Holy Methodius,
                Patriarch of Constantinople. Through God’s indulgence Leo the Isaurian, a
                swineherd and keeper of donkeys, inherited the scepter of the kingdom. At that
                time Saint Germanus was at the helm of the Church. Leo sent for him and said,
                “since it seems to me that there is no difference between the holy icons and
                idols, command that they be removed immediately from among us. Although if
                they are true likenesses of the saints, let them be hung higher on the walls so that
                we who are wallowing in sins do not defile them by venerating them.” But the
                Patriarch responded thus to the Emperor’s abomination, “O King, we have
                heard of someone who once raised his hand against the holy icons. He was called
                Conon. Could you be this man?” The emperor said, “I was so called as a child.”
                And since the Patriarch refused to obey the emperor, he deposed him and
                installed Anastasius, who sympathized with him. And so at that time began the
                struggle against the holy icons. After this Leo Constantine Copronymus became
                heir to the kingdom as well as to the savage attacks against the holy icons. And
                what can be said about the number and kind of deeds that lawless man
                committed except that he came to a most shameful end. His son, whose mother
                was a Khazar, inherited the kingdom after him, and he also came to a bad end.
                Irene and Constantine then ascended the throne. At the direction of the holy
                Patriarch Tarasius they assembled the Seventh Council, and the holy icons were
                once more accepted by Christ’s Church. After they relinquished the kingdom,
                Nicephorus ascended to the throne. After him there were Stauracius and then
                Michael Rhangabe, who were both iconoclasts. The beast-like Leo the Armenian
                seized the throne from Michael, and, having been misled by an impious hermit,
                began the second iconoclasm. And once more the Church was bereft of Her
                beauty. Michael Amorius succeeded him, whose son Theophilus then for the
                second time directed this madness against the icons. For it was this Theophilus
                who gave many of the Holy Fathers over to torments and tortures, seeking the
                truth about the holy icons and believing whatever he would. “If there be anyone
                in the city intent on uprising, then he will be caught not long after I am told.”
                And after reigning for 12 years, he was stricken with an intestinal disorder so that
                he desired to relinquish his life. His mouth opened so wide, that his internal
                organs were visible. The empress was so upset at what had happened, that she
                could barely sleep. And in a dream she beheld the most pure Theotokos holding
                the pre-eternal Child, surrounded by most luminous angels. They were striking
                Theophilus her husband and humiliating him. Now when her dream had passed
                and Theophilus had come to his senses, he cried, “Woe is me in my
                wretchedness, I am struck for the sake of the holy icons.” And immediately the
                empress held an icon of the Theotokos above him and entreated her with tears.
                And Theophilus, so inclined, saw that one of the clergy surrounding him had an
                engolpion, which he grabbed and kissed. Now as soon as his lips touched the
                icon, and he opened wide his mouth, he returned to normal and was relived of
                the adversity and affliction and fell asleep, after confessing that it is good to
                venerate the holy icons. Then the empress, fetching the holy and precious images
                from her bedchamber, convinced Theophilus to kiss them and venerate them
                with all his heart. A short while afterwards Theophilus departed this life.
                Theodora then commanded that all who were in exile and in prison be freed.
                John was deposed from the patriarchal throne, since he was more a sorcerer and
                demon worshiper than patriarch. Then Methodius, a confessor of Christ,
                ascended the throne, having suffered much through having been closed up in a
                tomb alive. While he was there, Ioannicius the Great, who was practicing
                asceticism on Mount Olympus, received a divine visitation. The great faster
                Arsaacius came to him and said, “God has sent me to you, that we might go to
                the righteous Isaiah the recluse in Nicomedia and learn from him what God
                desires and what is fitting for His Church.” Now when they came to the
                venerable Isaiah, he said to them, “Thus saith the Lord: Behold, the end is
                approaching for the enemies of My image. Go to the empress Theodora and to
                the Patriarch Methodius and tell them: “Cease to do what is not holy, and offer
                sacrifice to Me with the angels by venerating the countenance of My image and
                of the Cross”.” Hearing this they immediately left for Constantinople and
                announced what had been said to Patriarch Methodius and all God’s assembled
                people. The assembly then went to the empress and found her agreeable in all
                things, since this was the pious and God-loving tradition of the Fathers. The
                empress straightway brought out the image of the Theotokos for all to see, and
                venerating it, she said, “Let all be condemned who do not venerate the images,
                kissing them in love, not in worship as gods, but as images for the sake of the
                love of their archetypes. And they rejoiced with great joy. And in response she
                entreated them to pray for her husband Theophilus. Seeing her faith, they
                obeyed reluctantly. For Patriarch Methodius among the saints assembled all the
                people, priests and bishops and proceeded to God’s Great Church. Among the
                assembled were Joannicius the Great from Olympus, Arsaacius, Pancratius and
                the disciples of Theodore the Studite, and confessors Theophanes and Theodore
                Graptoi, Michael of the Holy City and Singelus and many others. And they
                prayed to God for Theophilus in tears all night long. Now this took place
                throughout the first week of the Great Fast, with the empress Theodora herself,
                the women and all the people taking part. Having completed the prayers, the
                empress Theodora retired at dawn on Friday, and dreamed that she was at the
                foot of the Cross, and there were several people passing noisily by, wearing
                various instruments of torture. As she recognized the Emperor Theophilus
                among those being led with his hands bound behind his back, she followed the
                group and its guards. When they reached the brass gates, she saw a supernatural
                vision, a man sitting in front of the image of Christ and Theophilus brought
                before him. Reaching to touch his feet, the empress prayed for the emperor. He
                opened his mouth and said, “Great is thy faith, O woman. Know that because of
                thy tears and thy faith, as well as the prayers and petitions of My servants and My
                priests, I grant forgiveness to thy husband Theophilus.” Then He said to the
                guards, “Loose him and give him to his wife.” And taking him, she departed
                rejoicing in gladness. And immediately the dream left her. Now Patriarch
                Methodius, while the prayers and petitions were being offered for him, had taken
                a new parchment scroll and written the names of all the heretical emperors,
                including Theophilus, placing it under the holy altar table. But on Friday he saw a
                great and terrible angel entering the temple, coming to him and saying, “Thy
                petition has been heard, O Bishop, and the Emperor Theophilus has received
                forgiveness. Trouble the Godhead about this no longer.” And desiring to
                ascertain the truth of his vision the Patriarch descended from his place, and
                taking the parchment and unrolling it, he found (O, the judgments of God!) that
                all reference to the name of Theophilus has been erased by God. Upon hearing
                this, the empress rejoiced greatly and requested the Patriarch to assemble all the
                people with the holy icons and crosses in the great church, so that might be
                adorned with the holy icons and God’s new miracle could be known by all. And
                soon when all had gathered in the church holding candles, the empress arrived
                with her son. And a Litiya was served there with the holy icons and the divine
                and precious wood of the Cross and with the sacred and divine Gospels. And
                leaving the church, calling out, “Lord, have mercy,” they processed the agreed
                mile. Then they returned to the church, where Divine Liturgy was celebrated.
                When the holy and precious icons were returned to their place, the holy men
                mentioned earlier and the pious Orthodox rulers were glorified, and those
                impious people who did not accept the honor of the holy icons were
                anathematized and condemned. And from that time these holy confessors
                appointed the annual commemoration of this solemnity, so that we might never
                again fall into a similar ignominy.
                O unchanging Image of the Father,
                through the prayers of Thy holy confessors,
                have mercy on us. Amen.
                ODE VII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: In the Persian furnace the youths ...
                Refrain: Glory to Thee our God, glory to Thee.
                Let the hosts of angels share in the joy of the Church, that with love and
                divine wisdom, they may cry aloud: “Blessed art Thou, O Lord, in the temple of
                Thy glory.”
                Refrain: Glory to Thee our God, glory to Thee.
                The triumphant assembly and Church of the firstborn rejoiceth now as it
                beholdeth the people of God with one accord crying aloud: “Blessed art Thou,
                O Lord, in the temple of Thy glory.”
                Glory ..., Delivered from the dark heresies of the past through the decision of
                the honored Empress Theodora, we cry aloud: “Blessed art Thou, O Lord, in the
                temple of Thy glory.”
                Now & Ever ..., O all-pure One, thou art exalted above the choirs on high,
                for alone among women thou hast become Mother of the Creator of all.
                Wherefore in joy we cry aloud: “Blessed art thou among women, O allimmaculate Lady.”
                Katavasia: In the Persian furnace the youths and descendants of Abraham,
                * burning with a love of piety * rather than by a flame of fire, * cried aloud
                saying: * Blessed art Thou in the temple of Thy glory, O Lord.
                ODE VIII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Stretching forth his hands ...
                Refrain: Glory to Thee our God, glory to Thee.
                Keeping the laws of the Church that we have received from the Fathers, we
                write icons, and with our lips and heart and we venerate them as we cry aloud: O
                all ye works of the Lord, bless ye the Lord.
                Refrain: Glory to Thee our God, glory to Thee.
                The honor and veneration shown to the icon, is ascribed to the prototype it
                represents, following the divinely-inspired teachings, wherefore with faith we cry
                aloud to Christ: O all ye works of the Lord, bless ye the Lord.
                Refrain: Let us bless Father, Son, Holy Spirit, the Lord!
                Her mind enlightened by the illumination of the divine Spirit, the honored
                Empress, filled with the fruits of divine wisdom, and with love of the splendor of
                Christ’s Church, along with all the faithful, blesseth Jesus, the God-Man.
                Now & Ever ..., Illumined by rays of noetic light, Thy holy house
                overshadoweth all with the cloud of the Spirit, and sanctifieth the faithful who
                sing with one accord: O all ye works of the Lord, bless ye the Lord.
                Refrain: We praise, bless and worship the Lord, chanting and supremely
                exalting Him throughout all ages.
                Katavasia: Having spread his hands, Daniel closed the lions jaws * in their
                den; * while the zealously pious youths, * girded with virtue, * quenched
                the power of the fire and cried aloud: * Bless ye the Lord, all ye works of
                the Lord.
                And then we chant the Hymn of the Most Holy Theotokos (the Magnificat)
                ODE IX
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion:
                Irmos: Christ, the Chief Cornerstone ...
                Refrain: Glory to Thee our God, glory to Thee.
                Seeing the honorable Church once more adorned with divinely-written
                images, let us make haste and with reverence cry aloud to God: We magnify
                Thee, O Thrice-Holy One.
                Refrain: Glory to Thee our God, glory to Thee.
                As a mark of glory and honor, the Church possesseth Thy Cross and the
                honorable icons, and depictions of the saints, and with joy and gladness O
                Master, she magnifieth Thee.
                Glory ..., Shine upon our rulers with Thy divine glory, O compassionate One,
                and encompass them about with the protection of the angelic hosts, bringing
                into subjection, the haughtiness of the heathen, O Master.
                Now & Ever ..., The condemnation of our first mother Eve hath been
                abolished, since thou, O pure One, beyond understanding, hast given birth to the
                Master of all; and now we kiss His likeness in the icons.
                Katavasia: A cornerstone not cut by hand O Virgin, * was cut from thee
                the unhewn mountain: * even Christ, Who hath joined together the
                disparate natures; * therefore rejoicing we magnify thee, * O Theotokos.
            """
            ,'exapostilarion': """
                Glory ..., from the Triodion, in Tone III:
                Leap for joy and clap your hands, * and with gladness sing aloud: * How
                strange and wonderful are Thy works, O Christ! * And who can tell of all Thy
                mighty acts, O Savior, ** Who hast united in harmony and with one accord the
                Church!
                Now & Ever ..., from the Triodion:
                The swords of hostile heresy now have failed, * and every memory of it, with
                all its tumult, hath vanished away. * For we see thy temple, O all-pure One, in all
                its splendor, * adorned with the grace of the precious icons, ** and we all are
                filled therewith.
            """
            ,'aposticha': """
                in Tone IV:
                Verse: Praise Him with tuneful cymbals, praise Him with cymbals of
                jubilation. * Let every breath praise the Lord.
                O Lover of mankind, * the Church now rejoiceth in Thee, her Bridegroom
                and Founder, * for by Thy divine Will Thou hast delivered her from the error of
                idolatry, * and by Thy precious Blood Thou hast betrothed her to Thyself. *
                With joy she accepts the restoration of the holy icons, * and with faith she sings
                in praise of Thee ** and in faith renders Thee glory.
                Verse: I will confess Thee, O Lord, with my whole heart, * I will tell of all
                Thy wonders.
                Having restored the representations of Thy flesh, O Lord, * affectionately
                kissing them, * we elucidate the great mystery of Thy dispensation. * For Thou
                didst not appear to us, O Lover of mankind, * merely in outward semblance, * as
                say the followers of Mani, * the enemies of God, * but in the full and true reality
                of the flesh; * and so the icons that depict Thy flesh ** lead us to the desire and
                love of Thee.
                Verse: I will be glad and rejoice in Thee, * I will sing to Thy name, O
                Most High.
                A feast of joy and gladness hath been revealed to us today. * For the dogmas
                of the true Faith shine forth, * rendering the Church of Christ bright with
                splendor, * adorning her with the holy icons * which have now been restored; **
                whereby God hath granted to the faithful unity of mind.
                Verse: Arise, O Lord my God, let Thy hands be lifted high; * forget not
                Thy paupers to the end.
                in Tone VI: Moses, in the season of abstinence, * received the Law and
                proclaimed it to the people. * Elijah by fasting closed the heavens; * and the
                three Children of Abraham through fasting overcame the lawless tyrant. * Count
                us also worthy, O Christ, * through fasting to attain the Feast of Thy
                Resurrection, as we cry aloud: ** Holy God, Holy and Strong One, and Holy
                Immortal One, have mercy on us.
            """
            ,'aposticha_theotokion': """
                Glory ..., in Tone VI:
                Moses, in the season of abstinence, * received the Law and proclaimed it to
                the people. * Elijah by fasting closed the heavens; * and the three Children of
                Abraham through fasting overcame the lawless tyrant. * Count us also worthy, O
                Christ, * through fasting to attain the Feast of Thy Resurrection, as we cry aloud:
                ** Holy God, Holy and Strong One, and Holy Immortal One, have mercy on us.
                Now & ever ..., in Tone II:
                Most Blessed art Thou, O Virgin Theotokos, * for through Him Who
                became incarnate of thee is Hades led captive, * Adam recalled, the curse
                annulled, Eve set free, death slain, * and we are given life. Wherefore, we cry
                aloud in praise: * Blessed art Thou, O Christ God, * Who hast been thus wellpleased, glory to Thee.
            """
            ,'apolytichia':"""

            """
        } #Matins
        ,'liturgy': {
            'beatitudes': [
                """
                    The Master’s countenance is depicted, honored with faith, and venerated;
                    whereby the Church regaineth her boldness before God, reverently glorifying the
                    Savior.
                """
                ,"""
                    The Church of Christ hath been delivered from the darkness of heresy:
                    putting on a robe of gladness, she is clothed in the light of divine grace.
                """
                ,"""
                    Glory ..., The Orthodox people have regained the light and glory which it had
                    of old, through the decree of the Empress Theodora and her pious son the
                    Emperor Michael.
                """
                ,"""
                    Now & Ever ..., He Who of old commanded Moses to make the ark of the
                    covenant, came to dwell within thee, as if in a noetic ark: He alone is supremely
                    glorified, making thy temple glorious with miracles.
                """
            ]
            ,'troparion':"""
                Troparion of the Feast, in Tone II:
                We venerate Thine immaculate icon, O good One, * asking the pardon of our
                transgressions, O Christ God. * For of Thine own will Thou wast well-pleased to
                ascend the Cross in the flesh, * that Thou mightest deliver from the slavery to
                the enemy those Whom Thou hast fashioned. * Therefore in thanksgiving we cry
                to Thee: * Thou didst fill all things with joy, O our Savior, ** when Thou camest
                to save the world.
            """
            ,'kontakion': """
                Kontakion from the Triodion, in Tone VIII:
                The uncircumscribed Word of the Father hath become circumscribed, *
                taking flesh from thee, O Theotokos, * and He hath restored the sullied image to
                its ancient glory, filling it with divine beauty. ** This our salvation we confess in
                deed and word, and we depict it in the holy icons.
            """
            ,'prokeimenon':"""
                Tone IV, The hymn of the Fathers: Blessed art Thou O
                Lord, the God of our Fathers, * and praised and glorified is Thy name
                unto the ages.
                Verse: For righteous art Thou in all which Thou hast done for us
            """
            ,'readings': """
                EPISTLE TO THE HEBREWS. (11:24 - 26, 32 - 40)
                Brethren: By faith Moses, when he was come to years, refused to be called
                the son of Pharaoh’s daughter; Choosing rather to suffer affliction with the
                people of God, than to enjoy the pleasures of sin for a season; Esteeming the
                reproach of Christ greater riches than the treasures in Egypt: for he had respect
                unto the recompence of the reward. And what shall I more say? for the time
                would fail me to tell of Gedeon, and of Barak, and of Samson, and of Jephthae;
                of David also, and Samuel, and of the prophets: Who through faith subdued
                kingdoms, wrought righteousness, obtained promises, stopped the mouths of
                lions. Quenched the violence of fire, escaped the edge of the sword, out of
                weakness were made strong, waxed valiant in fight, turned to flight the armies of
                the aliens. Women received their dead raised to life again: and others were
                tortured, not accepting deliverance; that they might obtain a better resurrection:
                And others had trial of cruel mockings and scourgings, yea, moreover of bonds
                and imprisonment: They were stoned, they were sawn asunder, were tempted,
                were slain with the sword: they wandered about in sheepskins and goatskins;
                being destitute, afflicted, tormented; (Of whom the world was not worthy:) they
                wandered in deserts, and in mountains, and in dens and caves of the earth. And
                these all, having obtained a good report through faith, received not the promise:
                God having provided some better thing for us, that they without us should not
                be made perfect.
                Alleluia from the Triodion, in Tone VIII:
                Verse: Moses and Aaron among His priests, and Samuel among them that
                call upon His name.
                Verse: They called upon the Lord, and He hearkened unto them.
                GOSPEL ACCORDING TO ST. JOHN (1:43-51)
                At the time: Jesus went forth into Galilee, and findeth Philip, and saith unto
                him, Follow me. Now Philip was of Bethsaida, the city of Andrew and Peter.
                Philip findeth Nathanael, and saith unto him, We have found him, of whom
                Moses in the law, and the prophets, did write, Jesus of Nazareth, the son of
                Joseph. And Nathanael said unto him, Can there any good thing come out of
                Nazareth? Philip saith unto him, Come and see. Jesus saw Nathanael coming to
                him, and saith of him, Behold an Israelite indeed, in whom is no guile! Nathanael
                saith unto him, Whence knowest thou me? Jesus answered and said unto him,
                Before that Philip called thee, when thou wast under the fig tree, I saw thee.
                Nathanael answered and saith unto him, Rabbi, thou art the Son of God; thou
                art the King of Israel. Jesus answered and said unto him, Because I said unto
                thee, I saw thee under the fig tree, believest thou? thou shalt see greater things
                than these. And he saith unto him, Verily, verily, I say unto you, Hereafter ye
                shall see heaven open, and the angels of God ascending and descending upon the
                Son of man.
                Communion Hymn: Praise the Lord from the heavens, praise Him in the
                highest.
                Another Verse: Rejoice in the Lord, O ye righteous; praise is meet for the
                upright. Alleluia, Alleluia, Alleluia.
            """
        } #Liturgy
    } #Service
    ,'-35': { #2nd Sunday | Gregory Palamas
        'vespers': {
            'stichera_tone': 'in Tone II:'
            ,'stichera': [
                """
                    With what hymns of praise shall we sing in honor of the holy hierarch? * He
                    is the trumpet of theology, * the fiery-inspired tongue of grace, * the honorable
                    vessel of the Spirit, * the unshaken pillar of the Church, * the beautification of
                    the inhabited earth, * the river of wisdom, the candlestick of the Light, ** the
                    clear star that renders bright the whole of creation.
                """
                ,"""
                    With what hymns of praise shall we sing in honor of the holy hierarch? * He
                    is the trumpet of theology, * the fiery-inspired tongue of grace, * the honorable
                    vessel of the Spirit, * the unshaken pillar of the Church, * the beautification of
                    the inhabited earth, * the river of wisdom, the candlestick of the Light, ** the
                    clear star that renders bright the whole of creation.
                """
                ,"""
                    With what chant shall we crown the holy hierarch * as with flowers? * He is
                    the champion of piety and the adversary of ungodliness, * the fervent protector
                    of the Faith, * the great guide and teacher, * the all-beauteous harp of the Spirit,
                    * the radiantly golden-tongued one, * a fountain flowing with the waters of
                    healing for the faithful, ** the great and right-wondrous Gregory.
                """
                ,"""
                    With what words shall we who dwell on earth * praise the archpaster? * He
                    is the teacher of the Church, * the preacher of the divine light, * the initiate of
                    the heavenly mysteries of the Trinity, * the beautification of the monastic life, *
                    renowned alike in action and in contemplation, * the glory of Thessalonica; *
                    The co-dweller in heaven ** with the divine and most glorious Martyr and
                    myrrh-gusher Demetrius.
                """
            ]
            ,'doxastichon': """
                in Tone VI:
                O thrice-blessed venerable saint, * most holy father, * good shepherd and
                disciple of Christ the Chief Shepherd, * having laid down thy life for thy sheep. *
                we ask of thee, O Gregory our god-bearing father, ** by thy prayers, may great
                mercy be granted to our souls.
            """
            ,'aposticha_theotokion': """
                Glory from the Triodion..., in Tone VIII:
                Thy tongue, spiritually healthy in teaching, * rings in the ears of our heart *
                awakening the souls of the slothful, * and thy divinely inspired words, * are
                found to be a ladder ascending from earth to God. * Wherefore O Gregory,
                wonder of Thessaly, * cease not pray to Christ that we who honor thee ** may
                be illumined with the divine light.
                Now & Ever ..., in Tone VIII:
                O unwedded Virgin! * thou who ineffably conceived God in the flesh, *
                Mother of God Most High: * accept the supplications of thy servants, O allimmaculate one, * granting unto all cleansing of transgressions; * and, accepting
                now our supplications, ** pray thou that we all be saved.
            """
        } #Vespers
        ,'matins': {
            'troparion': """
                Glory ..., Troparion for the Saint, in Tone VIII
                The light of Orthodoxy, support and teacher of the Church, * glory of
                monastics and invincible protector of theologians, * O wonderworker Gregory
                praise of Thessalonica and preacher of grace, ** pray thou without ceasing that
                our souls be saved.
                Now & ever ..., in Tone VIII:
                O Good One, Who for our sake wast born of the Virgin * and, having
                endured crucifixion, cast down death by death, * and as God revealed the
                resurrection: * disdain not that which Thou hast fashioned with Thine own hand.
                * Show forth Thy love for mankind, O Merciful One; * Accept the supplications
                of the Theotokos who bore Thee, ** and save Thy despairing people, O our
                Savior!
            """
            ,'after50': """
                in Tone VIII:
                Glory ..., The gates of repentance, do Thou open unto me, O Giver of Life,
                * for early in the morning my spirit seeketh Thy holy temple, * bearing the
                temple of my body all defiled. * But as One who art compassionate * cleanse it
                by Thy loving-kindness and mercy.
                Now & ever ..., Guide me on the paths of salvation, O Theotokos: * for I
                have polluted my soul with shameful deeds * and wasted all my life in
                slothfulness. * but by thine intercessions * do thou deliver me from all impurity.
                In Tone VI:
                Have mercy upon me, O God, * according to Thy great mercy: * and
                according to the multitude of Thy compassion * blot out my transgressions.
                In Tone VIII: As I the wretched one ponder the multitude of evil deeds I
                have done, * I tremble for fear of the dread day of judgment. * But trusting in
                Thy compassionate mercy, * like David do I cry unto Thee: * “Have mercy upon
                me, O God, according to Thy great mercy”.
            """
            ,'canon': """
                ODE I
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion, in Tone VIII:
                Irmos: The wonderworking staff of Moses ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                Shedding fervent tears, with the words of the Prodigal we fall down before
                Thee O God and Father of all, saying: “We have sinned, departing far from
                Thee, we have made ourselves the slaves of prodigality; do Thou accept our
                repentance”.
                Refrain: Have mercy on me, O God, have mercy on me.
                I have wasted the royal birthright Thou didst confer upon me, by becoming,
                a man for my sake O Word: and I have been bitterly condemned to feed swine,
                with my taste for things sinful. But do Thou spare me, O Savior, in Thy
                compassion.
                Refrain: Have mercy on me, O God, have mercy on me.
                I kneel before Thee, as did the Prodigal Son of old, O Lord and Master: do
                Thou run out to meet me and receive me, and taking me in Thine embrace grant
                me the tokens of Thy salvation. Instead of a hired servant, O Lover of mankind,
                make me once again thy son.
                Refrain: Most Holy Theotokos save us.
                Theotokion: Human nature was granted to be worthy of God’s revelation
                through thee, O blessed joyous one, for thou art the only mediator, O Virgin,
                between God and man; meet it is that we glorify thee, since thou art the Mother
                of God.
                Of Saint Gregory in Tone IV:
                Irmos: I shall open my mouth ...,
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                O divine orators, and chosen theologians, all ye tongues inspired by God,
                come and unite together, that ye may rightly sing in praise of the herald of the
                Spirit. the divine Gregory,
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                The pillar of the Faith, the champion of the Church, let us praise the great
                Gregory, the most tireless shepherd of Thessalonica, the true glory of the
                episcopate.
                Glory ..., From childhood thou didst desire the higher life of perfection, O
                father, and from thy youth thou didst love wisdom, showing thyself to be a true
                follower and companion of thy namesake Gregory the Theologian.
                Now & Ever ..., O all-immaculate one, be thou to me a path in life, guiding
                me to the divine dwelling-place. For I have wandered astray and stumbled into
                the pit of evil: do thou lead me back from this by thine intercessions.
                Katavasia in Tone IV: I shall open my mouth, * and be filled with the
                Spirit, * and utter discourse to the Queen and Mother; * and be seen
                radiantly keeping festival, * joyfully praising her wonders.
                ODE III
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion:
                Irmos: O Christ strengthen me on the rock ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I am filled with fear when I consider my actions, and how far I have
                departed from Thee, wasting thy wealth in prodigal desires, wherefore in
                repentance I cry to Thee, my Father and God: “I have sinned, do Thou save
                me”.
                Refrain: Have mercy on me, O God, have mercy on me.
                Sinning on earth, I am in fear of heaven; for it will be my accuser, O Word,
                when all shall stand before Thee and submit to Thy righteous judgment.
                Refrain: Have mercy on me, O God, have mercy on me.
                I fed myself on dark and defiled thoughts when I left thee, O Savior, and
                went into a far country to live prodigally; but now I cry: “I have sinned against
                Thee, I have sinned; save me, who fleeth to Thy tender mercy”.
                Refrain: Most Holy Theotokos save us.
                Theotokion: Adam’s nature was rendered godlike, O Virgin: For from thy
                womb God hath assumed flesh; by which we were freed from the ancient
                condemnation, having been deceived of old by the hope of becoming gods.
                Of Saint Gregory in Tone IV:
                Irmos: O Theotokos, thou living and plentiful fount ...,
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                Holding fast to the harp of thy divinely inspired teaching, we flee from
                every innovation of the heretics, and we slay all of them with thy holy writings, O
                Gregory.
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                The foolish wisdom of the heretics hast thou destroyed O blessed one,
                bearing the hypostatic Wisdom of God in thy heart, by which thou didst
                triumphantly defeat their putrid innovations.
                Glory ..., O most wise one, thou didst put to death every carnal desire of the
                flesh, and through thine ascetic activities enlivened the activity of thy soul, and
                by this thou hast been revealed to be a divine instrument of theology.
                Now & Ever ..., With full knowledge and by mine own free choice, I have
                eagerly desired a shameful and prodigal life; but do thou bind my heart with
                divine love by thy holy intercessions, O Virgin and Bride of God.
                Katavasia: O Theotokos, thou living and plentiful fount, * establish in
                spiritual fellowship those who sing hymns to thee, * and in thy divine
                glory * grant them crowns of glory.
                Kontakion of the Triodion, in Tone IV:
                The season of virtuous action is now upon us, * the Judge is at the door. Let
                us arise and observe the Fast, * offering tears of compunction, and with
                almsgiving let us cry aloud: * We have sinned more than there be grains of sand
                in the sea; * but, do Thou spare us O creator of all, ** that we may receive
                crowns of incorruption.
                Sessional Hymns of Triodion, in Tone IV:
                Thou didst burn up the deceptions of the heretics, and didst well elucidate
                the Orthodox faith, thereby enlightening all the world; showing thyself to be
                triumphantly victorious, a pillar of the Church and a true hierarch; cease not to
                intercede before Christ, that we all be saved.
                Glory ..., Now & Ever ..., in Tone IV:
                Quickly receive our prayers, O Lady, and bring them to thy Son and God, O
                all-immaculate Sovereign Lady; extinguish the blasphemies of the evil-tongued
                heretics; bring to naught their devices, and cast down the impudence of the
                ungodly who make war against thy servants, O most pure One.
                ODE IV
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion:
                Irmos: Thou, O Lord, art my strength ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                The wealth of Thy fatherly commandments which Thou hast granted me, I
                have wasted in living a life of sensual pleasure; I, the wretched one, am now
                poor, stripped of my former divine gifts, wherefore, I repent and confess; turn
                not away from me, O Master and Lord.
                Refrain: Have mercy on me, O God, have mercy on me.
                Graciously hast Thou taken upon Thyself my poverty, I who of old, was
                exiled far from Thee, assuming my human nature within Thyself, and sanctifying
                me O Lover of mankind; Thy divine body O Word, is my calling to be joyous.
                Refrain: Have mercy on me, O God, have mercy on me.
                With unceasing tears, may we be delivered from the everlasting torments
                that God hath prepared for the evil spirits, let us cry like the Prodigal: We have
                sinned against Thee, O Father, but do Thou accept us all, for we take refuge in
                Thy mercy.
                Refrain: Most Holy Theotokos save us.
                Theotokion: The Word, Who is co-beginningless with the Father and the
                Spirit, hath been born from a Virgin who knew not a man, yet without
                undergoing change, remaining what He was, yet preserving for ever what He
                hath taken from us; for He is one Son in two natures, preserving the essence of
                each.
                Of Saint Gregory in Tone IV:
                Irmos: Seated in glory ...,
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                Thou hast opened thy mouth, O wise father, and preached the divine
                Wisdom which thou hast ever learnt in thy heart; and which showed Balaam to
                be vainly lacking in understanding and foolish.
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                Thou hast set beneath the earth, O most sweetest Sun, in accordance with
                the laws of nature, but in the morning thou shalt rise again with Christ, the Sun
                that knoweth no evening, Who doth watch over all by thine intercessions.
                Glory ..., The grace of God hath been manifest in thee, O blessed one, the
                great glory and strong support of the Orthodox, the good shepherd, and second
                Theologian, and brave guardian of thy flock.
                Now & Ever ..., Open the ears of my soul, O Mother of God, for thou hast
                given birth to the Lord who once opened the ears of the deaf; enable us to hear
                the Word of God and keep it.
                Katavasia: He who sitteth in glory upon the throne of the Godhead, *
                Jesus the true God, * is come in a swift cloud * and with His sinless hands
                he hath saved those who cry: * Glory to Thy power, O Christ.
                ODE V
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion:
                Irmos: O never-setting Light ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                Having rejected the wealth and divine gifts conferred upon me, I have come
                to a country cursed by a famine of the gifts of life; but, O Father, for the sake of
                Thy tender compassion, restore to me the glory and the joy that of old was once
                mine.
                Refrain: Have mercy on me, O God, have mercy on me.
                Let us who have spent our life in prodigal living, take up the resolve of the
                Prodigal, and with undoubting faith and a compunctionate heart, flee to the
                merciful Father, that we may receive the remission of our sins.
                Refrain: Have mercy on me, O God, have mercy on me.
                Tarry not, O my soul, dwelling exiled in a far country, but run swiftly to thy
                God and Father confessing thy sins; that thou mayest receive forgiveness for the
                wicked things thou hast done, having wasted thy life in vanity.
                Refrain: Most Holy Theotokos save us.
                Theotokion: Thou art a noetic cloud of light, bearing within thee the Sun of
                righteousness. O most-holy Virgin, Who hath dispelled the dark ignorance of
                idolatry, and hath enlightened us with the light of true knowledge.
                Of Saint Gregory in Tone IV:
                Irmos: All creation stands in awe of thy divine glory ...,
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                With the sickle of thy words and with thy holy writings thou didst cut down
                the thorns of heresy, and spit out the tares of falsehood, sowing the seeds of
                Holy Orthodoxy, O archpaster Gregory.
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                O all-wise one, thy words and sacred writings are to those who draw near to
                them; a heavenly dew, honey from the rock, the bread of angels, nourishing
                food, and sweetness, O Gregory, thou fount of living water.
                Glory ..., The earth and sea acknowledge thee to be their common teacher, a
                holy pillar of Orthodoxy, and a sacred and honorable armory of divine dogmas, a
                most wise and saintly theologian, and a companion and equal to the apostles.
                Now & Ever ..., With the waters of compunction wash the filth from my
                heart, O immaculate one, and bestow upon me an image of repentance through
                thy holy prayers to our compassionate God, Whom thou didst ineffably bear.
                Katavasia: All creation stands in awe of thy divine glory; * for thou, O
                Virgin who hast not known wedlock, * didst contain within thy womb the
                God of all, * and gave birth to the timeless Son, * bestowing peace, upon
                all who hymn thee.
                ODE VI
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion:
                Irmos: Have mercy upon me O Savior ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I was Thy younger son, and wasted the wealth Thou gavest me, withdrawing
                far from Thee into an iniquitous life; and am now deprived of Thy blessings, O
                Lover of mankind. I come To Thee, O my Father and God, asking forgiveness.
                Refrain: Have mercy on me, O God, have mercy on me.
                I have been rewarded to dwell in a cruel exile, and am condemned to feed
                swine, for I have wasted the riches that Thou graciously gavest me; and I am
                stripped of everything. But since Thou art my God, have compassion upon me.
                Refrain: Have mercy on me, O God, have mercy on me.
                Having sinned, I have no boldness, O Lover of mankind, to look up to
                heights of heaven, nor call myself Thy son, prodigal that I am. But do Thou Who
                hast boundless mercy, be quick to have compassion upon me.
                Refrain: Most Holy Theotokos save us.
                Theotokion: Beyond description is thy childbearing, and ineffable is the
                manner of thy birth-giving, O Virgin maiden, for transcending understanding
                thou hast given birth to God, and yet preserved thy virginity inviolate.
                Wherefore, as is meet, we all glorify thee as in truth, the very Theotokos.
                Of Saint Gregory in Tone IV:
                Irmos: : As we celebrate this sacred and solemn feast ...,
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                The vain innovations and language of foolish Balaam were shattered by the
                words, teachings, and sharp-minded understanding of the most wise Emperor
                and of thee, O Gregory.
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                The divine harp of the Spirit, the trumpet that plainly proclaimed the divine
                mysteries, the ruling archpaster of Thessalonica, the theologizing tongue, let us
                honor in hymns.
                Glory ..., As once the people were led by a pillar of fire, likewise thou hast
                burnt up the enemies of the Faith, and illumined the congregation of the faithful,
                O divinely wise Gregory our father.
                Now & Ever ..., Be unto me, O all-holy Lady, quietness and a haven of
                consolation; lead me into the safe harbor of divine refuge, calming the tempest
                of my passions.
                Katavasia: As we celebrate this sacred and solemn feast of the Theotokos ,
                * let us come, clapping our hands, * O people of the Lord, * and give
                glory to God who was born of her.
                Kontakion of the Saint, in Tone VIII:
                Holy and divine instrument of the highest wisdom, * joyful trumpet of
                theology, * with one accord we sing thy praises, O Gregory thou divinely
                inspired one. * But since thy mind standest before the original Mind, ** guide
                our minds to Him, O father, * that we may cry to thee: Rejoice, thou preacher of
                grace.
                Ikos: Thou hast appeared on earth as an angelic messenger, proclaiming
                unto mortal men the mysteries of God. Endowed with a human mind and flesh,
                yet speaking with the voice of the bodiless powers, thou hast filled us with
                amazement, O divinely inspired saint, impelling us to cry aloud to thee: Rejoice,
                For through thee darkness is dispelled: Rejoice, For through thee light hath
                returned. Rejoice, Messenger of the uncreated Godhead: Rejoice, Reprover of
                created folly. Rejoice, Height impossible to climb, that telleth us of God’s nature:
                Rejoice, Depth hard to fathom, that speaks of His energy. Rejoice, For thou hast
                rightly proclaimed God’s glory: Rejoice, For thou hast denounced the opinions
                of the wicked. Rejoice, Torch that reveals the Sun: Rejoice, Cup filled with
                nectar. Rejoice, For through thee truth hath shone forth: Rejoice, For through
                thee falsehood hath been plunged in darkness. Rejoice, Preacher of grace!
                SYNAXARION READING
                Verse: Now is the truly great preacher of the Radiant Light ...,
                Verse: Led by the Source of Light to the never-setting Light.
                This son of the divine and never-setting Light was a true man of God
                indeed, and a wondrous servant and minister of the divine mysteries, having
                been born in the imperial city (Constantinople) of most radiant and glorious
                parents. Through his virtue and instruction he desired to adorn not only the
                outer of mankind according to the senses, but also much of the unseen inner
                being. When he was yet quite young, his father died. His mother, brothers and
                sisters raised him and instructed him in morals, catechism and sacred scripture,
                and sent him to teachers of worldly wisdom, from whom he learned well.
                Cleverly combining his learning with a natural zeal, he soon became skilled in
                verbal arts. At the age of twenty, regarding all earthly things as inferior and
                passing dreams, he sought recourse to God the Author and Giver of all wisdom,
                to consecrate his entire self to God through a perfect life. Hence he disclosed his
                great love for God, his pious intentions and burning desire to his mother, and he
                found that for a long she too had been desirous of this and rejoiced at his
                decision. And straightway gathering her children his mother said with joy,
                “Behold, I and the children God has given me!” And she disclosed to them the
                intent of the great Gregory, asking if it seemed to them to be good. And he with
                words of instruction soon convinced them all in earnestness to follow him in his
                love and withdrawal from life. Distributing then his earthly possessions to the
                poor according to the teachings of the Gospel, and cheerfully abandoning human
                love, earthly honor and the approbation of men, he followed after Christ. Placing
                his mother and sisters in a convent, he and his brothers went to the sacred
                Mount Athos, where he convinced his brothers to stay in different monasteries,
                so that they would have no time to be together, thereby perfecting their life in
                God. He himself became obedient to a wondrous man named Nicodemus who
                had consecrated his life of silence to God alone. Learning from him through
                actions every precept and every virtue, through a mystical revelation there he
                received the protection of the all pure Theotokos, an invincible help in all things.
                After Nicodemus’ parting from this life to God, having lived for several years in
                the Great Lavra most zealously with perfection of thought and a love of silence,
                Gregory left the Lavra and embraced the wilderness. Increasing ever in love and
                always desiring to be with God, he dedicated himself to a life of utmost severity,
                strenghtening his reasoning with earnest attention, raising his thoughts to God,
                practising prayer at all times, meditating on divine things, and leading an
                excellent life. With the help of God he overcame the attacks of demons, and
                cleansing his soul with fountains of tears at all night vigils, he became a chosen
                vessel of the gifts of the Spirit of God, and often had visions of the Godhead.
                Wondrously, because of the commencement of attacks of the Ishmaelites on
                Thessalonica, he retreated to the summit skete, and was constrained to speak
                with several of the citizenry. Having led a diligent life, for he was no longer
                young, and having cleansed his body and soul entirely, at God’s command, he
                received the great anointing to the priesthood, and like an angel, becoming
                trancendent in the celebration of the sacred mysteries, so that all who observed
                him were moved. He was truly great and was recognized as a bearer of the Spirit
                by those who lived godly lives, revealing himself to those who witnessed the
                following outward signs: He had authority over demons and was able to release
                those possessed from their wiles and deceit. He could change barren trees into
                fruitful ones. He foresaw things to come, and was blessed with other gifts and
                fruits of the Divine Spirit. For when it lies within our power to act upon the
                virtues, then we are not able to fall into temptation. Without the virtues there can
                be no perfection or appearance of faith in God (for, he says, action and passion
                descending together perfects a man in goodness after God), but frequent falls
                into various temptations, made this man great, so that he is shown to be perfect
                to all. And what mind can think on this further? What more can be said? First
                the licentious wiles of the evil contender. And then the lies and slanders of the
                new theomachists were directed at him. In all twenty-three years he endured
                much anger and affliction. For the Italian beast, Varlaam of Calabria,
                philosophized in a worldly manner, and through the vanity of his philosophy (for
                he thought to know everything) he mounted a fierce attack against Christ’s
                Church, against our faith and against those who openly professed it. For the
                grace of the Father, the Son and the Holy Spirit is one and the light of the age to
                come, as also the righteous shine like the sun, as Christ Himself demonstrated
                beforehand in splendor on the mountain. And simply he erroneously taught that
                all the power and action of the Godhead in three hypostases and all differences
                there might be in the divine nature were created, and those who piously believed
                that the divine Light was uncreated, and all His power and action, as not to one
                new of that which is naturally in God, through his rhetoric and widespread
                letters, he called bitheists and polytheists, as the Jews, Savelius and Arius call us.
                For the sake of these the divine Gregory, as a defender of piety and most
                glorious intercessor, fought before everyone and was reviled. He was sent by the
                Chruch to Constantinople, and he went. And when the most divine emperor
                Andronicus, fourth after the Paleologos, sought to defend the faith, a sacred
                council was assembled. And when Varlaam appeared with his previously
                mentioned impious teachings and his accusations against piety, the great
                Gregory, filled with the Spirit of God and clothed with invincible power from on
                high, stopped his mouth from speaking against God and disgraced him utterly.
                With words of spiritual fire and documents he burned Varlaam’s heresies like
                brushwood to ashes. Wherefore unable to endure the shame, the enemy of piety
                ran back to Italy, whence he came. Immediately after this the council exposed his
                great harm, and with arguments to the contrary dispersed his compostions. But
                those who had partaken of these ideas did not cease their struggle against God’s
                Church. For this cause through the great urging of the sacred council, the
                emperor himself, and most importantly the command of God, Gregory was
                persuaded to ascend the bishop”s throne, and was appointed the pastor of the
                sacred Church in Thessalonica. Wherefore he bravely and steadfastly
                accomplished great deeds in behalf of the Orthodox Faith. But many evil heirs of
                Acindinus and Varlaam appeared, fierce beasts born of ferociousness, as well as
                their teacings and compositions, not once, not twice, not three times, but many
                times in great quantity, and not during the reign of one emperor or patriarch but
                during three successive reigns and an equal number of patriarchates and many
                councils, which through divinely inspired words and writings, countered them in
                many ways, and eventually overcame them completely. And some persist, having
                no regard for the High Court, shamelessly attacking the saints who triumphed
                over them. Such were in short Gregory’s victories over the impious. Then God,
                in an ineffable manner, sent the teacher to the East. He was sent as the elder
                from Thessalonika to Constantinople to make peace between two quarreling
                emperors. But he was seized by the Haggarenes and for an entire year was made
                to travel in suffering from place to place, from city to city, fearlessly preaching
                the Gospel of Christ. And he affirmed and convinced them in their faith,
                entreating them to remain steadfast, confirming with divine wisdom those who
                were wavering in the faith or could not understand or asked questions about the
                previous events, and freely granting healing to those who asked it. To those who
                did not believe, to wretched apostates, to those who had followed them and
                those who cast aspersions on our teachings about the incarnate providence of
                our Lord and God, or the veneration of the precious Cross and the holy icons he
                spoke many times without hesitation. He spoke also of Mohammed and
                answered many other questions which they put to him. Some wondered in
                themselves, others were angered and put forth their hands and would have made
                him a martyr, if not for God’s plan and the promise of money to be gained from
                his ransom. So he was spared. Then the great saint was freed by the lovers of
                Christ, and this bloodless martyr returned once more in joy to his flock. In
                addition to the other many and great gifts and preeminent qualities, which he
                had, he was also adorned with the wounds of Christ, bearing also in himself
                Christ’s, according to Paul. Let us describe him; these were his characteristics.
                Along with his excellence he was meek and humble. (We do not speak here of
                God and divine matters, for he was quite a defender of these.) He did not
                remember evil and was good-natured, desiring to return good for evil. He never
                quarreled. He was always patient and magnanimous in the face of adversity. He
                was above vanity and sensuality. He was always temperate and not extravagant in
                all personal necessities, and for all that time he was not ill. He endured quietly
                and silently, always graciously, to the limits of what was done to him, so that all
                would see him as reasonable, attentive and keen witted. And consequently he
                never allowed his eyes to be void of tears, but sympathized with a flow of tears.
                And so like a martyr from the beginning to the end he struggled against demons
                and the passions, driving heretics far the Christ’s Church, defining the Orthodox
                Faith through his words and compositions, and by them as with a seal sealing all
                divinely inspired writing, for his life and word became a seal of the life and words
                of the saints. He tended his flock for thirteen years more in the godly manner of
                the Apostles, and having adorned them with his moral teachings, he guided them
                to the heavenly sheepfold. And having served all Orthodox, both those who
                lived during his time and those yet to be born, he was translated to the higher
                life, having lived sixty-three years in all. And he commended his spirit into the
                hands of God, leaving his body to his flock, as a special portion and a precious
                treasure, enlightened and glorified at the end.
                For every day Christ benefits with wonders those who come near in faith
                and grants healing of many diseases,
                many of whom tell of their cures.
                Through His prayers, O God,
                have mercy on us. Amen.
                ODE VII
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion:
                Irmos: The fire in Babylon once stood in awe ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I lack the boldness to call myself Thy son, O man-befriending Father; but I
                beseech Thee that I may be as one of Thy hired servants. Reject me not who
                doth cry out to Thee: O God of our fathers, blessed art Thou.
                Refrain: Have mercy on me, O God, have mercy on me.
                We have defiled our former life by this present life, and have thereby lost
                our former nobility. But let us hasten to our only Father and God, and with
                fervent repentance, let us receive salvation.
                Refrain: Have mercy on me, O God, have mercy on me.
                Cruel is the citizen whom I, the wretched one, am condemned to serve; the
                hunger which I endure, while feeding the swine, is severe and insufferable. But I
                beseech Thee, O Savior, cause me to turn back, and have mercy on me.
                Refrain: Most Holy Theotokos save us.
                Theotokion: Our nature which was once deadened, hast thou restored to
                life, O Virgin Theotokos, who alone didst bear Life; wherefore we the faithful
                acknowledge the salvation wrought by thee, who in the flesh didst give birth to
                the God of our fathers.
                Of Saint Gregory in Tone IV:
                Irmos: The Holy Children bravely trampled ...,
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                Those who study thy words of instruction and thy writings, O Gregory, are
                initiated into the knowledge of God, and filled with the noetic Wisdom of God;
                they theologize concerning His uncreated grace and energy.
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                The sword and the bow of the heretics, didst Thou destroy, O great
                Hierarch along with the pride of Balaam, and all the power of heresy, as the web
                of a spider is torn apart by a stone.
                Glory ..., The faith of the pious hath been sealed by thy words and dogmas;
                and the boldness of heresy hath ceased, O Gregory, bringing to an end the
                suppression of Orthodoxy, and the might of the heretics.
                Now & Ever ..., We truly believe that thou art a fount of water, from which
                we, withered by the sickness of the passions, draw forth the divine water of
                salvation, wherefore we cry aloud, O all-pure one; “blessed is the fruit of thy
                womb”.
                Katavasia: Refusing to worship created things * in place of the Creator, *
                the divinely wise youths bravely trampled down the threatening fire * and
                rejoicing they sang aloud: * O supremely hymned Lord and God of our
                Fathers, Blessed art Thou.
                ODE VIII
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion:
                Irmos: In his wrath the Chaldean Tyrant ...
                Refrain: Have mercy on me, O God, have mercy on me.
                We who believe in Thee know the wealth of Thy great and boundless
                compassion, O Master. Wherefore we fervently bow down before Thee with the
                Prodigal, receive us who have sinned and flee to Thee for refuge, for there is no
                sin, O compassionate One, that can overcome Thy love for mankind.
                Refrain: Have mercy on me, O God, have mercy on me.
                For the sake of compassion, Thou didst humble Thyself, O Master, and
                draw near to Thy fallen sons. For in Thy love for mankind Thou dost go out to
                meet the fallen, and embracing and kissing them Thou hast granted them
                salvation: And if one reproacheth Thee for this, as One merciful, Thou art not
                angered with him, for Thou art the Lover of mankind.
                Refrain: Have mercy on me, O God, have mercy on me.
                Most fearful will be the judgment passed upon me, O Master; for though I
                see that Thou art longsuffering and a Lover of mankind, I flee not to Thee nor
                call upon Thee with the words of the Prodigal, instead I pass the course of my
                life in slothfulness; be Thou merciful to me, and save me from condemnation, O
                compassionate One, for the sake of my penitence.
                Refrain: Let us bless Father, Son, and Holy Spirit, the Lord!
                We glorify not three Gods but one Godhead; in very truth we honor three
                Hypostases, the Father unbegotten, the Son begotten from the Father, and the
                Holy Spirit proceeding from the Father. One God in Three; and with faith we
                glorify each with the title of God.
                Refrain: Most Holy Theotokos save us.
                Theotokion: From the multitude of tribulations that beset me, O allimmaculate One, and the tempest of sorrows that overwhelm me, do thou, by
                thine intercessions, deliver me to the calm haven of salvation, and from all
                dangers save me, as thou art a fervent protector, that I may worthily glorify thee
                as the Theotokos throughout all ages.
                Of Saint Gregory in Tone IV:
                Irmos: The offspring of the Theotokos ...,
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                Thou standest now before the throne of the all-merciful One, one in
                likeness to the Theologians, and as one their equal, O all-wise Gregory, hierarch
                of Thessalonica, glory of the episcopate, adorned with the dignity of the high
                priesthood, ever serving God.
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                Knowing the purity of thine understanding, even before thy conception in
                the womb; God clearly revealed to the faithful Emperor that thou wouldst be an
                invincible champion of the Church; wherefore, by canonical consecration, thou
                wast sealed with the chrism of the high priesthood.
                Refrain: Let us bless Father, Son, Holy Spirit, the Lord!
                Thou didst clearly defeat and vanquish the faction of Akindynos, by the
                wisdom of thy teaching O glorious Gregory, Bishop of Thessalonica, and as
                smoke vanisheth, so didst thou vanquish their putrid foolishness by the
                thunderous voice of thy divine theology.
                Now & Ever ..., In thy womb, O Virgin, didst the Word of God, in His
                extreme goodness, restore the nature of man, which had been crushed beneath
                the passions, wholly renewing and sanctifying it. Wherefore being saved by thee,
                we glorify thee throughout all ages.
                Refrain: We praise, we bless, we worship the Lord, praising and
                supremely exalting Him throughout all ages.
                Katavasia: The offspring of the Theotokos * saved the Holy Children in
                the furnace. * He who was then prefigured hath now been born on earth, *
                and He gathereth all creation to hymn thee: * all ye works praise ye the
                Lord * and supremely exalt Him throughout all ages
                And then we chant the Hymn of the Most Holy Theotokos (the Magnificat)
                ODE IX
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion:
                Irmos: Heaven stood amazed ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                For my sake, Thou hast sacrificed the fatted calf, fill Thou now my thirsty
                soul with joy and gladness: I who was once lost, do Thou receive again. I who
                was once dead, do Thou Lead back to life, and having placed the divine robe of
                salvation upon me, clothe me with incorruption.
                Refrain: Have mercy on me, O God, have mercy on me.
                O ye souls which have wandered far from God, and are deprived of the
                divine gifts, come and with fervor turn back like the Prodigal and cry: O good
                Father Who art in the heavens, we have all sinned against Thee; do Thou be
                merciful to us and save us, for unto Thy mercy do we flee for refuge.
                Refrain: Have mercy on me, O God, have mercy on me.
                Since Thou art abundantly rich in compassion, loathe me not O Lord, O
                Lord, I have wasted my wealth in a multitude of pleasures, but fleeing to Thee, I
                cry aloud with the voice of the Prodigal: “I have sinned against Thee, do Thou
                save me who now flees to Thy mercy.
                Refrain: Most Holy Theotokos save us.
                Theotokion: I thy servant, have thee as my haven of salvation, and guide
                and protection; since thou art good, do thou entreat God, that I may be delivered
                from all tribulations and temptations, O Lady, for with love, I have placed all my
                hope in thee
                Of Saint Gregory in Tone IV:
                Irmos: Let every mortal born on earth ... ,
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                A mirror divine wast thou, O Gregory, for in accordance with the divine
                image, thou hast kept thyself undefiled; and manfully establishing thy mind as
                master over the passions of the flesh, thou hast attained to that which is in
                accordance with God’s likeness. Wherefore thou hast become the most glorious
                dwelling-place of the Holy Trinity.
                Refrain: Holy Hierarch Father Gregory, pray to God for us.
                Like an inspired winged angel, thou dist come to the aid of the pious
                Emperor, as one completely filled with the Holy Spirit, fighting against the vainminded Balaam, who in his madness unjustly spake against the God of heaven;
                Wherefore thou didst justly gain the victory over him.
                Glory ..., Wholly filled with heavenly wisdom, thou didst shine forth upon
                the world as light, teaching the dogmas of Orthodoxy. Befriending thyself to and
                loving Wisdom, O most wise one, thou didst conceive the fear of God within
                thyself, giving birth to the words of the Spirit.
                Now & Ever ..., We and all the faithful with one accord offer to thee a
                hymn of thanksgiving, for thou hast freed us from the ancient curse, O
                Birthgiver of God; by which we have gained through thee God’s blessing,
                salvation, enlightenment and mercy, and eternal joy.
                Katavasia: Let every mortal born on earth, * radiant with light, in spirit
                leap for joy; * and let the host of the angelic powers * celebrate and honor
                the holy feast of the Mother of God, * and let them cry aloud: * Rejoice! O
                Theotokos, thou pure Ever-Virgin.
            """
            ,'exapostilarion': """
                Glory ..., from the Triodion, in Tone III:
                Rejoice, glory of the fathers, voice of theologians, * tabernacle of inward
                stillness, * dwelling-place of wisdom, greatest of teachers, * deep ocean of the
                Word. * Rejoice, thou who hast practiced the virtues of the active life * and
                ascended to the heights of contemplation; * Rejoice, healer of man’s sickness.
                Rejoice, shrine of the Spirit; ** Rejoice, father who though dead art still alive.
                Now & Ever ..., from the Triodion:
                Theotokion: O Sovereign Lady, Queen of all creation, * higher than all the
                heavenly hosts, * stretch out thy regal hand and preserve the world; * bless the
                priests who liturgize in thine honor * and forgive those monastics who entreat
                thy prayers. * Grant peace to all people who dwell in thy courts. * Strengthen
                those in war during the time of battle. * Protect this thy holy city. * Count us
                worthy to see the heavenly Kingdom and the gates of Paradise, * when at the
                Second Coming the Judge shall sit on His dread throne to judge all the earth, **
                O Queen of the angels.
            """
            ,'aposticha': """
                a from the Triodion, in Tone I:
                Verse: Praise Him with tuneful cymbals, praise Him with cymbals of
                jubilation. * Let every breath praise the Lord.
                In the world thou didst live a life of blessedness, * and now in heaven thou
                dost rejoice in the assembly of the blessed; * because thou wast meek, thou
                dwellest now in the land of the meek, O hierarch Gregory. * God hath made
                thee rich in the grace of working miracles, ** which thou dost bestow on those
                who honor thee.
                Verse: I will confess Thee, O Lord, with my whole heart, * I will tell of
                all Thy wonders.
                O blessed saint, thou didst plant the dogmas of Orthodoxy, * cutting down
                the thorns of heresy, * multiplying well the seeds of faith * by feeding them with
                the waters of thy words, * and as an active husbandman thou hast brought to
                God ** ears of wheat increased an hundredfold.
                Verse: I will be glad and rejoice in Thee, * I will sing to Thy name, O
                Most High.
                The bright glory of thy blameless life, O blessed saint, * hath amazed both
                angels and men. * For with steadfast purpose thou hast labored in the ascetic life,
                * showing thyself to be a worthy hierarch and minister of God, ** and His true
                friend.
                Verse: Arise, O Lord my God, let Thy hands be lifted high; * forget
                not Thy paupers to the end.
                Tone VI: Upon those walking in the darkness of sin, O Christ, * Thou hast
                shone forth as a guiding light * in this season of abstinence. * Do Thou also
                show unto us * the fragrant day of Thy Passion, * that we may cry unto Thee: **
                Arise, O God, and have mercy on us.
            """
            ,'aposticha_theotokion': """
                Glory ..., Sticheron from the Triodion, in Tone VI:
                Upon those walking in the darkness of sin, O Christ, * Thou hast shone
                forth as a guiding light * in this season of abstinence. * Do Thou also show unto
                us * the fragrant day of Thy Passion, * that we may cry unto Thee: ** Arise, O
                God, and have mercy on us.
                Now & ever ..., in Tone II:
                Most Blessed art Thou, O Virgin Theotokos, * for through Him Who
                became incarnate of thee is Hades led captive, * Adam recalled, the curse
                annulled, Eve set free, death slain, * and we are given life. Wherefore, we cry
                aloud in praise: * Blessed art Thou, O Christ God, * Who hast been thus wellpleased, glory to Thee
            """
        } #Matins
        ,'liturgy': {
            'beatitudes': [
                """
                    Holding fast to the harp of thy divinely inspired teaching, we flee from
                    every innovation of the heretics, and we slay all of them with thy holy writings, O
                    Gregory.
                """
                ,"""
                    The foolish wisdom of the heretics didst thou destroy O blessed one,
                    bearing the Hypostatic Wisdom of God in thy heart, by which thou didst
                    triumphantly defeat their putrid innovations.
                """
                ,"""
                    Glory ..., O most wise one, thou didst put to death every carnal desire of the
                    flesh, and through thine ascetic activities didst enliven the activity of thy soul,
                    and by this thou wast revealed to be a divine instrument of theology.
                """
                ,"""
                    Now & Ever ..., With full knowledge and by mine own free choice, I have
                    eagerly desired a shameful and prodigal life; but do thou bind my heart with
                    divine love by thy holy intercessions, O Virgin and Bride of God.
                """
            ]
            ,'troparion':"""
                Troparion for the Saint, in Tone VIII:
                The light of Orthodoxy, support and teacher of the Church, * glory of
                monastics and invincible protector of theologians, * O wonderworker Gregory
                praise of Thessalonica and preacher of grace, ** pray thou without ceasing that
                our souls be saved.
            """
            ,'kontakion': """
                Glory ..., Kontakion for the Saint, in Tone VIII:
                Holy and divine instrument of the highest wisdom, * joyful trumpet of
                theology, * with one accord we sing thy praises, O Gregory thou divinely
                inspired one. * But since thy mind standest before the original Mind, guide our
                minds to Him, O father, ** that we may cry to thee: Rejoice, thou preacher of
                grace.
                Now & Ever ..., Lenten Kontakion, in Tone VIII:
                The season of virtuous action is now upon us, * the Judge is at the door. Let
                us arise and observe the Fast, * offering tears of compunction, and with
                almsgiving let us cry aloud: * We have sinned more than there be grains of sand
                in the sea; * but, do Thou spare us O creator of all, ** that we may receive
                crowns of incorruption.
            """
            ,'prokeimenon':"""
                Prokeimenon, in Tone V: Thou, O Lord, shalt keep us and shalt
                preserve us from this generation and for evermore.
                Verse: Save me, O Lord, for a righteous man there is no more.
                Prokeimenon for the Saint in Tone I: My mouth shall speak wisdom, *
                and the meditation of my heart shall be of understanding.
            """
            ,'readings': """
                EPISTLE TO THE HEBREWS (DAY) (1:10 - 2:3)
                Brethren: The Lord, in the beginning hast laid the foundation of the earth;
                and the heavens are the works of thine hands: They shall perish; but thou
                remainest; and they all shall wax old as doth a garment; And as a vesture shalt
                thou fold them up, and they shall be changed: but thou art the same, and thy
                years shall not fail. But to which of the angels said he at any time, Sit on my right
                hand, until I make thine enemies thy footstool? Are they not all ministering
                spirits, sent forth to minister for them who shall be heirs of salvation? Therefore
                we ought to give the more earnest heed to the things which we have heard, lest
                at any time we should let them slip. For if the word spoken by angels was
                stedfast, and every transgression and disobedience received a just recompence of
                reward; How shall we escape, if we neglect so great salvation; which at the first
                began to be spoken by the Lord, and was confirmed unto us by them that heard
                him;
                EPISTLE TO THE HEBREWS (7:26 - 8:2)
                Brethren: For such an high priest became us, who is holy, harmless,
                undefiled, separate from sinners, and made higher than the heavens; Who
                needeth not daily, as those high priests, to offer up sacrifice, first for his own
                sins, and then for the people’s: for this he did once, when he offered up himself.
                For the law maketh men high priests which have infirmity; but the word of the
                oath, which was since the law, maketh the Son, who is consecrated for evermore.
                Now of the things which we have spoken this is the sum: We have such an high
                priest, who is set on the right hand of the throne of the Majesty in the heavens;
                A minister of the sanctuary, and of the true tabernacle, which the Lord pitched,
                and not man.
                Alleluia, in the Tone of the week. Then:
                For the Saint, Alleluia, in Tone 2: The mouth of the righteous shall
                meditate wisdom, and his tongue shall speak of judgment.
                GOSPEL ACCORDING TO ST. MARK (2:1-12)
                At that time: Jesus entered into Capernaum after some days; and it was
                noised that he was in the house. And straightway many were gathered together,
                insomuch that there was no room to receive them, no, not so much as about the
                door: and he preached the word unto them. And they come unto him, bringing
                one sick of the palsy, which was borne of four. And when they could not come
                nigh unto him for the press, they uncovered the roof where he was: and when
                they had broken it up, they let down the bed wherein the sick of the palsy lay.
                When Jesus saw their faith, he said unto the sick of the palsy, Son, thy sins be
                forgiven thee. But there was certain of the scribes sitting there, and reasoning in
                their hearts, Why doth this man thus speak blasphemies? who can forgive sins
                but God only? And immediately when Jesus perceived in his spirit that they so
                reasoned within themselves, he said unto them, Why reason ye these things in
                your hearts? Whether is it easier to say to the sick of the palsy, Thy sins be
                forgiven thee; or to say, Arise, and take up thy bed, and walk? But that ye may
                know that the Son of man hath power on earth to forgive sins, (he saith to the
                sick of the palsy,) I say unto thee, Arise, and take up thy bed, and go thy way into
                thine house. And immediately he arose, took up the bed, and went forth before
                them all; insomuch that they were all amazed, and glorified God, saying, We
                never saw it on this fashion.
                GOSPEL ACCORDING TO ST. JOHN (10:9-16)
                The Lord said unto the Jews who came to Him: I am the door, by me if any
                man enter in, he shall be saved, and shall go in and out, and find pasture. The
                thief cometh not, but for to steal, and to kill, and to destroy: I am come that they
                might have life, and that they might have it more abundantly. I am the good
                shepherd: the good shepherd giveth his life for the sheep. But he that is an
                hireling, and not the shepherd, whose own the sheep are not, seeth the wolf
                coming, and leaveth the sheep, and fleeth: and the wolf catcheth them, and
                scattereth the sheep. The hireling fleeth, because he is an hireling, and careth not
                for the sheep. I am the good shepherd, and know my sheep, and am known of
                mine. As the Father knoweth me, even so know I the Father: and I lay down my
                life for the sheep. And other sheep I have, which are not of this fold: them also I
                must bring, and they shall hear my voice; and there shall be one fold, and one
                shepherd.
            """
        } #Liturgy
    } #Service
    ,'-28': { #3rd Sunday | Adoration of the Cross
        'vespers': {
            'stichera_tone': ''
            ,'stichera': [
                """
                    Shine, O Cross of the Lord, * shine the lightning rays of thy grace, into the
                    hearts of those who honor thee. * With god-pleasing love, we embrace thee, O
                    desire of all the world. * Through thee our tears of sorrow have been wiped
                    away; * we have been delivered from the snares of death and have passed over to
                    unending joy. * Show us the glory of thy beauty * and grant us thy servants the
                    reward of our abstinence, ** for we entreat with faith thy rich protection and
                    great mercy.
                """
                ,"""
                    Rejoice! O life-giving Cross, * the fair Paradise of the Church, * Tree of
                    incorruption that hath brought unto us the enjoyment of eternal glory: *
                    Through thee the hosts of devils have been driven back; * the hierarchies of
                    angels rejoice, * and the congregations of the faithful keep festival. * Thou art an
                    invincible weapon, an unshakable stronghold; * thou art the victory of the
                    faithful and the glory of priests. ** Grant us now to reach the Passion of Christ
                    and His great mercy
                """
                ,"""
                    Rejoice! O life-giving Cross, unconquerable trophy of piety, * door to
                    Paradise, foundation of the faithful, * rampart set about the Church. * Through
                    thee the curse hath been utterly destroyed, * the power of death hath been
                    swallowed up, * and we have been raised from earth to heaven: * Invincible
                    weapon, and adversary of demons, * glory of the martyrs, * true adornment of
                    holy monks, * haven of salvation ** bestowing great mercy upon the world.
                """
                ,"""
                    Come, O first created twain, * ye who fell from the choir on high * through
                    the envy of the murderer of mankind, * when of old with bitter pleasure * ye
                    tasted from the tree in Paradise. * Behold, the Tree of the Cross revered by all, *
                    now draweth near! * Run with haste and embrace it joyfully, * and cry unto it
                    with faith: * O precious Cross, thou art our calling; * O divinely blessed Tree, *
                    partaking of thy fruit we have gained incorruption; * we are restored once more
                    to Eden, ** and have received great mercy.
                """
            ]
            ,'doxastichon': """
                From the Triodion, in Tone III:
                O Christ our God, of Thine own Will Thou didst accept Crucifixion, * for
                the sake of the general resurrection of the race of mankind. * Taking the quill of
                the Cross, with bloody fingers * Thou hast signed our absolution in the red ink
                of royalty. * We are in danger once again of being parted from Thee; * Forsake
                us not! Take pity on Thy people in distress, * for Thou alone art long-suffering. *
                Rise up and fight against those who fight against us, ** since Thou art allpowerful.
            """
            ,'aposticha_theotokion': """
                in Tone IV:
                O Lord Thou didst enable meek David * to defeat the foreigner, * come
                Thou to the aid of Thy faithful people, * and by the weapon of the Cross cast
                down our enemies. * In Thy compassion show us Thy mercy as of old, * that
                they may know, that in truth Thou art God, * and that we who put our trust in
                Thee shall conquer. * By the constant mediations of Thy most pure Mother, **
                grant us Thy great mercy.
            """
        } #Vespers
        ,'matins': {
            'troparion': """
                Glory ... Troparion of the Cross, in Tone I:
                Save O lord Thy people * and bless thine inheritance. * Grant now unto the
                faithful, * victory over adversaries, * and by the power of Thy Cross ** do Thou
                preserve Thy commonwealth.
                Now & ever ..., in Tone I:
                When Gabriel announced to thee, “Rejoice!”, O Virgin, * the Master of all
                became incarnate within thee, the holy tabernacle, * at his cry, as the righteous
                David said. Thou wast shown to be more spacious than the heavens, * having
                borne thy Creator. * Glory to Him Who made His abode within thee! * Glory to
                Him Who came forth from thee! ** Glory to Him Who hath set us free by thy
                birthgiving.
            """
            ,'after50': """
                in Tone VIII:
                Glory ..., The gates of repentance, do Thou open unto me, O Giver of Life,
                * for early in the morning my spirit seeketh Thy holy temple, * bearing the
                temple of my body all defiled. * But as One who art compassionate * cleanse it
                by Thy loving-kindness and mercy.
                Now & ever ..., Guide me on the paths of salvation, O Theotokos: * for I
                have polluted my soul with shameful deeds * and wasted all my life in
                slothfulness. * but by thine intercessions * do thou deliver me from all impurity.
                In Tone VI:
                Have mercy upon me, O God, * according to Thy great mercy: * and
                according to the multitude of Thy compassion * blot out my transgressions.
                In Tone VIII: As I the wretched one ponder the multitude of evil deeds I
                have done, * I tremble for fear of the dread day of judgment. * But trusting in
                Thy compassionate mercy, * like David do I cry unto Thee: * “Have mercy upon
                me, O God, according to Thy great mercy”.
            """
            ,'canon': """
                ODE I
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion, in Tone I:
                Irmos: It is the Day of Resurrection, * let us be radiant, O ye people; *
                Pascha, the Lord’s Pascha: * for from death to life, * and from earth to
                heaven, * Christ God hath brought us, ** as we sing the song of victory.
                Refrain: Glory to Thy Precious Cross, O Lord.
                This is a day of festivity: by the arising of Christ, death hath been shown to
                be impotent and the light of life hath dawned; Adam hath arisen and danceth for
                joy. Therefore let us cry aloud and sing a song of victory.
                Refrain: Glory to Thy Precious Cross, O Lord.
                This is the day of the veneration of the Precious Cross, shining with the
                effulgence of Christ’s Resurrection, come unto it all ye peoples, and let us kiss it
                with great rejoicing in our souls.
                Refrain: Glory to Thy Precious Cross, O Lord.
                O mighty Cross of the Lord, manifest thyself: show me the divine vision of
                thy beauty, and grant me to worthily venerate thee. For as One living, I speak to
                thee and embrace thee.
                Refrain: Glory to Thy Precious Cross, O Lord.
                Let heaven and earth give praise with one accord, for the all-blessed Cross
                hath now been set forth before all, on which Christ’s Body was affixed when
                sacrificed. Let us embrace it with great rejoicing in our souls.
                Glory ..., O Trinity of Hypostases, O Unity of Essence, the Father, Son and
                Spirit, equal in power, one in purpose and will, one in dominion and rule, watch
                over Thy world and grant it peace.
                Now & Ever ..., O Virgin who hath not known a man, without seed thou
                hast given birth to a Child: In purity didst thou carry and give birth to the Maker
                of all, Christ our God. Entreat Him to grant peace to the world.
                Katavasia in Tone I: Moses the servant of God * prefigured Thy Cross in
                the days of old, * when he divided the Red Sea with his rod * and led
                Israel across on dry land; * and he sang a song of deliverance unto Thee,
                O Christ our God.
                ODE III
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion, in Tone I:
                Irmos: Come, let us drink a new drink, * not one miraculously brought
                forth from a barren rock * but the Fountain of Incorruption, * springing
                forth from the tomb of Christ, * in Whom we are strengthened.
                Refrain: Glory to Thy Precious Cross, O Lord.
                O come, let us sing a new song, celebrating the overthrow of Hades, for
                Christ hath arisen from the grave; taking death captive, and saving all the world.
                Refrain: Glory to Thy Precious Cross, O Lord.
                O come, ye faithful, and let us drink, not from a well-spring pouring forth
                perishable water, but from the fountain of light, as we venerate the Cross of
                Christ, in which we glory.
                Refrain: Glory to Thy Precious Cross, O Lord.
                Of old, that which Moses prefigured with his outstretched arms, Thy Cross;
                we now we kiss in adoration, putting to flight the noetic Amalek, O Master
                Christ, and by which we gain salvation.
                Refrain: Glory to Thy Precious Cross, O Lord.
                O ye faithful, with pure eyes and lips let us sing a song of gladness, joyfully
                venerating the Cross of the Lord, lauding it with hymns.
                Glory ..., I honor one beginningless God, One in three Hypostasis,
                undivided in Essence, the Father, the Son and the Spirit of life, in Whose Name
                we were baptized.
                Now & Ever ..., In days of old Moses saw thy mystery prefigured in the
                bush, O pure One: As it was not consumed by the flames, so did thy womb
                remain unconsumed by the fire of the Godhead.
                Katavasia: By Thy Cross, O Christ Master, * set me firmly on the rock of
                the faith: * Let not my mind be shaken by the assaults * of the malicious
                enemy; * for Thou alone art holy.
                Sessional Hymns of the Cross in Tone VI:
                Thy Cross, O Lord, sanctifieth, and bringeth healing * to those sickened by
                sins. * Through it we fall down before Thee: ** have mercy upon us.
                Verse: Exalt ye the Lord our God and worship at His footstool, for He
                is holy.
                Today the word of the Prophet hath been fulfilled: * Behold! we worship at
                the place on which Thy feet have stood, O Lord, * and tasting from the Tree of
                salvation, * we have been delivered from our sinful passions * by the
                intercessions of the Theotokos, ** O Thou only Lover of mankind.
                Glory ..., No sooner, O Christ, hath the wood of the Cross been set up, *
                than the foundations of death hath been shaken O Lord. * Hades swallowed
                Thee eagerly, * but it let Thee go with trembling. * Thou hast shown us Thy
                salvation, O Holy One, * and we glorify Thee, O Son of God; ** have mercy
                upon us.
                Now & Ever ..., O Virgin Theotokos, entreat thy Son, * willingly nailed
                upon the Cross, * and risen from the dead, Christ our God, * that our souls may
                be saved.
                ODE IV
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion, in Tone I:
                Irmos: On divine watch let the God-inspired Habakkuk stand with us, *
                and show forth the light-bearing angel clearly saying: * Today salvation is
                come to the world, * for Christ is risen * as Almighty.
                Refrain: Glory to Thy Precious Cross, O Lord.
                “Behold, Christ is risen,” saith the Angel to the myrrh-bearing women.
                “Lament not, but go and say to the apostles: Rejoice! today is the salvation of the
                world; for through His death the tyranny of the enemy hath been destroyed.”
                Refrain: Glory to Thy Precious Cross, O Lord.
                As we celebrate today the joyful veneration of Thy life-giving Cross, O
                Christ, we prepare ourselves for Thine all-holy Passion; for Thou hast brought to
                pass the salvation of the world, as Thou art all-powerful.
                Refrain: Glory to Thy Precious Cross, O Lord.
                There is joy today in heaven and on earth, for the sign of Christ hath been
                made manifest to the world, the thrice-blessed Cross; which hath been set before
                us, as a fount of ever-flowing joy to all who venerate it.
                Refrain: Glory to Thy Precious Cross, O Lord.
                What shall we offer Thee, O Christ? For Thou hast given us Thy Precious
                Cross to venerate, upon which Thine all-holy Blood was shed, to which Thy
                flesh was affixed by nails, and which we kiss with adoration giving thanks to
                Thee.
                Glory ..., I sing the praises of the Three Hypostasis in one Godhead; I
                proclaim one simple Nature undivided: Father eternal, Son and Holy Spirit, one
                in throne and lordship, one single Kingdom, one everlasting Power.
                Now & Ever ..., In thee alone among women, O pure One, hath been
                revealed something marvelous and awesome: Thou hast renewed nature,
                conceiving without seed, yet remaining as before, a virgin; for the Child that thou
                hast borne is true God.
                Katavasia: Seeing Thee, O mighty Lord, upon the Cross, * the sun was
                seized with fear and hid its rays, * with dread the whole creation glorified
                Thy longsuffering, * and the earth was filled with Thy praise.
                ODE V
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion, in Tone I:
                Irmos: Let us awake in the deep dawn, * and instead of myrrh, offer a
                hymn to the Master, * and we shall see Christ, * the Sun of Righteousness,
                * Who causeth life to dawn for all.
                Refrain: Glory to Thy Precious Cross, O Lord.
                From the tomb hath arisen the never-setting Effulgence, shining upon the
                world the light of incorruption, O compassionate One, drive out the sorrow of
                death from the farthest ends of the earth.
                Refrain: Glory to Thy Precious Cross, O Lord.
                Cleansed by abstinence let us draw near, and with fervor let us kiss in
                adoration the all-holy Wood upon which Christ hath been crucified, thus saving
                the world O Compassionate One.
                Refrain: Glory to Thy Precious Cross, O Lord.
                The ranks of angels dance with gladness, for today we venerate Thy Cross.
                by which Thou hast shattered the hosts of devils O Christ, and saved mankind.
                Refrain: Glory to Thy Precious Cross, O Lord.
                The Church hath been revealed as another Paradise, having within it, like
                the first Paradise of old, a Tree of life, Thy Cross, O Lord. By which, touching it,
                we partake of immortality.
                Glory ..., I glorify three co-eternal Hypostases, in one Essence, the Father,
                Son and Spirit, a single Three-sunned Light, one Power and Kingdom,
                unmingled in characteristics.
                Now & Ever ..., Thou hast conceived according to the law of nature, yet
                above that law; for thou alone hast seedlessly borne a child. Strange and fearful it
                is to contemplate or speak of thy birth-giving, O all-immaculate One.
                Katavasia: Rising early in the morning * we sing Thy praises, O Savior of
                the world, * for we have found peace through Thy Cross. * By it Thou hast
                renewed mankind, * and led us to the never-waning light..
                ODE VI
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion, in Tone I:
                Irmos: Thou didst descend into the nethermost parts of the earth, * and
                didst shatter the eternal bars that held the fettered, O Christ, * and on the
                third day, * like Jonah from the whale, * Thou didst arise from the tomb.
                Refrain: Glory to Thy Precious Cross, O Lord.
                Thou didst arise O Christ, and trample upon death as a King almighty;
                Thou didst recall us from the vaults of Hades to the enjoyment of the Kingdom
                of Heaven, in the land of immortality.
                Refrain: Glory to Thy Precious Cross, O Lord.
                O ye faithful, let us cry aloud with divine songs, chanting triumphantly to
                God, as we kiss the Cross of the Lord; for it is a fount of holiness to all those in
                this world.
                Refrain: Glory to Thy Precious Cross, O Lord.
                The words of the Psalmist have been fulfilled: for behold! we worship at the
                footstool of Thy most pure feet, O all-powerful One, before Thy Precious Cross,
                the threefold-beloved Wood.
                Refrain: Glory to Thy Precious Cross, O Lord.
                In the prophesies of the Lamenter we see the Tree, enclosed and bearing
                Thy fruit; Thy Cross O merciful One, and kissing it with adoration, we chant in
                praise of Thy bonds and tomb, the spear and nails.
                Refrain: Glory to Thy Precious Cross, O Lord.
                That which Thou wast pleased to bear upon Thy shoulders, the Holy Cross,
                and upon which Thou didst accept to be raised, and crucified in the flesh, we kiss
                with adoration; receiving from it strength against our invisible foes.
                Glory ..., I praise the Unity in three Hypostases and the Trinity worshipped
                in one Nature, the Triune God, three-sunned Light, the Father, Son and Holy
                Spirit.
                Now & Ever ..., O undefiled Ewe-lamb, a wonder greater than all wonders
                hath been revealed in thee: For thou hast borne the Lamb that taketh away the
                sins of the world, fervently entreat Him on behalf of those who sing thy praises.
                Katavasia: Jonah in the belly of the whale * foreshadowed with his
                outstretched hands * the figure of the Cross; * and he leapt out from the
                sea-monster, * saved by Thy power, O Word.
                Kontakion from the Triodion, in Tone VII:
                The fiery sword no longer guardeth the gates of Eden, * for it hath been
                wondrously quenched by the wood of the Cross. * The sting of death and the
                victory of Hades have been vanquished, * for Thou art come, O my Savior,
                crying unto those in Hades: ** “Enter again into Paradise.”
                Ikos of the Cross: Pilate set up three crosses in the place of the Skull, two
                for the thieves and one for the Giver of Life. Seeing Him, Hades cried to those
                below: “O my servants and my powers! Who is this that hath fixed a nail in my
                heart? A wooden spear hath suddenly pierced me, and I am rent asunder.
                Inwardly I am in pain; and anguish hath seized my senses. My spirit is troubled,
                and I am constrained to cast out Adam and his posterity. A tree brought them to
                me, but now the Tree of the Cross leadeth them back again to Paradise.”
                SYNAXARION READING
                Verse: Let all the earth venerate the Cross,
                Verse: Through which it has learned to worship Thee, the Word.
                On this third Sunday of the Great Fast we celebrate the Veneration of the
                precious and life-giving Cross. Since during the forty days of the Fast we are also
                in a way crucified, mortified to the passions, contrite, abased and despondent,
                the precious and life-giving Cross is offered to us as refreshment and
                confirmation, calling to mind the Passion of our Lord Jesus Christ and
                comforting us. If our God was crucified for our sake, how great should be our
                effort for His sake, since our afflictions have been assuaged through the Lord’s
                tribulations, and by the commemoration and the hope of the Cross of glory. For
                as our Savior in ascending the Cross was glorified through dishonor and grief, so
                should we also endure our sorrows, in order to be glorified with Him. Also, as
                those who have traveled a long hard road, weighed down by the labors of their
                journey, in finding a shady tree, take their ease for a moment and then continue
                their journey rejuvenated, so now in this time of the Fast, this sorrowful and
                laborious journey, the Holy Fathers have planted the life-giving Cross, for our
                relief and refreshment, to encourage and make easier the labors that lie ahead. Or
                as when there is a royal procession, the king’s scepter and banners precede him,
                and then he then himself appears, radiant and joyous in his victory, causing his
                subjects to rejoice with him. So then our Lord Jesus Christ, desiring to show His
                sure victory over death and His glory on the day of the Resurrection, sends His
                scepter before Himself, the sign of His kingship, the life-giving Cross, to gladden
                and refresh us, as it greatly fortifies and enables us to be prepared to receive the
                King with all possible strength, and to praise Him in His radiant victory. This
                week lies at the middle of the holy Forty Day Fast. The Fast is like a bitter source
                because of our contrition and the sadness and sorrow for sin that it brings. And
                as Moses plunged the branch in the bitter waters of Marah, making them sweet,
                so God, Who has led us through the spiritual Red Sea away from Pharaoh,
                through the life-giving wood of the precious and life-giving Cross, sweetens the
                bitterness of the Forty Day Fast, and comforts us as those who were in the
                wilderness, up until the time when by His Resurrection He will lead us to the
                spiritual Jerusalem. And since the Cross is called, and indeed is, the Tree of Life,
                it is the very tree that was planted in the Garden of Eden. So it is fitting that the
                Holy Fathers have planted the Tree of the Cross in the middle of the Forty Day
                Fast to commemorate both Adam’s tasting of its sweet fruit and of its being
                taken from us in favor of the Tree of the Cross, tasting of which we shall in no
                way die, but will have even greater life.
                Through the power of Thy Cross, O Christ our God,
                preserve us also from the temptations of the Evil One.
                And make us worthy to venerate
                Thy divine Passion and life-bearing Resurrection,
                having radiantly traversed the great length of the Fast,
                and have mercy on us, as Thou art good and lovest mankind. Amen.
                ODE VII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion, in Tone I:
                Irmos: He Who delivered the Children from the furnace, * became man,
                and suffered as a mortal, * and through His Passion * clothed mortality
                with the beauty of incorruption, * He is the only blessed and supremely
                glorified * God of our fathers.
                Refrain: Glory to Thy Precious Cross, O Lord.
                Thou didst arise from the tomb on the third day, as one awakening from
                sleep, O Lord, and by Thy divine power didst slay the gatekeepers of Hades;
                raising up all our ancestors from ages past, O Thou only blessed and supremely
                glorified God of our fathers.
                Refrain: Glory to Thy Precious Cross, O Lord.
                O ye peoples, let us with song and dance express our joy, and greatly rejoice
                at the veneration of the Cross, giving glory to Christ Who was nailed thereon, the
                only blessed and supremely glorified God of our fathers
                Refrain: Glory to Thy Precious Cross, O Lord.
                Thou hast shown the instrument of death to be a source of life, wherefore it
                is worshiped throughout the whole world. Thy Cross, O all-merciful One, doth
                sanctify those who worship it, O Thou only blessed and supremely glorified God
                of our fathers.
                Refrain: Glory to Thy Precious Cross, O Lord.
                Thou alone art merciful and compassionate, O Thou only Jesus: illumine
                and sanctify those who venerate and with faith worship Thy Cross and Thy
                divine Passion, O Thou only blessed and supremely glorified God of our fathers.
                Glory ..., I praise the Godhead, a Unity in three Hypostases: For the Father
                is Light, the Son is Light, and the Spirit is Light, but the Light remaineth
                undivided, shining forth in a unity of essence, but in the three rays of its
                Hypostases.
                Now & Ever ..., Thou wast proclaimed by all the prophets, by a multitude
                of names: For thou hast been revealed to be the gateway of God, the golden
                vessel of manna, the holy land, O Virgin Bride of God who hast conceived in the
                flesh Jesus Christ, the only blessed and supremely glorified God of our fathers..
                Katavasia: The Lord Who delivered the Children from the flames * took
                flesh and came upon the earth; * nailed to the Cross, He hath granted us
                salvation, * He Who alone is blessed and supremely glorified, * the God of
                our fathers.
                ODE VIII
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion, in Tone I:
                Irmos: This chosen and holy day * is the first of the Sabbaths, * the queen
                and lady, * the feast of feasts, * and the festival of festivals, * wherein we
                bless Christ throughout the ages.
                Refrain: Glory to Thy Precious Cross, O Lord.
                “Why do ye hold sweet-smelling spices in your hands? Whom are ye
                seeking?,” crieth the angel at the tomb. “Christ our God hath arisen, raising up
                the nature of mortal man from the vaults of Hades.”
                Refrain: Glory to Thy Precious Cross, O Lord.
                Rejoice, O Cross, the Wood threefold-rich in divinity, a light unto those in
                darkness. Shining upon the four corners of the earth, preparing us to see the
                longed for Arising of Christ. Grant that all the faithful may be found worthy to
                reach Pascha.
                Refrain: Glory to Thy Precious Cross, O Lord.
                On this day, the Wood of the Cross of Christ, anointed with life, filleth the
                world with the fragrant myrrh of divine grace. Let us smell its God-given
                fragrance, venerating it with faith throughout the ages.
                Refrain: Glory to Thy Precious Cross, O Lord.
                Come, Elisha the prophet, and tell us plainly: What was the wood that thou
                didst cast into the water? Was it not the Cross of Christ, which draweth us up
                from the depths of corruption? and which we faithfully venerate throughout the
                ages.”
                Refrain: Let us bless Father, Son, Holy Spirit, the Lord!
                I glorify one Essence in three beings: the Father, Son and Spirit, neither
                commingled in Hypostases nor divided in Nature; for there is but one God in a
                Trinity, ruling over all throughout the ages.
                Now & Ever ..., Alone among mothers, hast thou remained a virgin, O Mary
                Bride of God. Without knowing a man thou didst give birth to the Savior Christ,
                yet kept the seal of thy virginity intact; wherefore we the faithful call thee blessed
                throughout the ages.
                Refrain: We praise, we bless, we worship the Lord, praising and
                supremely exalting Him throughout all ages.
                Katavasia: Daniel, great among the prophets, * was cast into the lions’
                den; * but, stretching out his hands in the form of the Cross, * he was
                delivered from their mouths and kept unharmed, * blessing Christ our
                God throughout the ages.
                And then we chant the Hymn of the Most Holy Theotokos (the Magnificat)
                ODE IX
                The appointed Canons from the Oktoechos. Then:
                The Canon from the Triodion, in Tone I:
                Irmos: Shine, shine, O new Jerusalem, * for the glory of the Lord hath
                arisen upon thee; * dance now and be glad, O Zion, * and do thou exult,
                O pure Theotokos, ** in the arising of Him Whom thou didst bear.
                Refrain: Glory to Thy Precious Cross, O Lord.
                Thou didst descend into the tomb, O God the Giver of Life, and didst
                smash all the fetters and gates therein, raising up the dead who cry aloud: Glory
                to Thine Arising, O Christ, the all-powerful Savior.
                Refrain: Glory to Thy Precious Cross, O Lord.
                Thy tomb, O Christ, hath brought life to me: for Thou, the Lord of life,
                hath come and cried unto those dwelling in the grave: “O all ye who are in
                bonds, be ye loosed, for I the Redeemer of the world have come.”
                Refrain: Glory to Thy Precious Cross, O Lord.
                With songs, all ye trees of the forest dance and be glad, beholding your
                fellow-tree, the Cross, being adored and venerated today: for Christ hath been
                exalted upon it in the highest, as the divine David prophesied.
                Refrain: Glory to Thy Precious Cross, O Lord.
                I died through a tree, but I have found in thee a Tree of Life, O my Cross of
                Christ. Thou art my invincible protector, mine unshakable defense against the
                demons. Venerating thee this day, I cry aloud: Sanctify me by thy glory.
                Glory ..., I worship Thee, as a Trinity of Hypostases in a Unity of Essence,
                the Father, the Son and the Holy Spirit, one Power and Kingdom, reigning over
                all creation.
                Now & Ever ..., Thou art the great mountain, O Virgin, wherein Christ
                dwelt, as the divine David saith. By thee we are raised up to heaven, regaining
                sonship by adoption through the Spirit, O all-blessed One.
                Katavasia: O Virgin Mother and true Theotokos, * who without seed didst
                bear Christ our God, * Who wast lifted in the flesh upon the Cross. * We
                and all the faithful, as is meet, * magnify thee with thy Son.
            """
            ,'exapostilarion': """
                Glory ..., from the Triodion, in Tone III:
                Seeing the Precious Cross of Christ placed before us this day, * let us in
                faith rejoice and kiss it with love, * and ask the Lord Who wast willingly crucified
                thereon, * to deem us all worthy to worship the precious Cross, ** and attain to
                the Resurrection uncondemned.
                Now & Ever ..., the Theotokion from the Triodion:
                Before the Tree, upon which for our sake, O all-pure One, * thy Son,
                stretched out His most pure hands and was nailed thereto, * we now fall down
                and with true devotion, worship. * Grant unto us peace, that we may come to the
                most precious and world-saving Passion; * and that may we worship at the
                radiant feast of Pascha, * the Lord’s Day which bringeth light and joy ** to all
                creation.
            """
            ,'aposticha': """
                in Tone IV:
                Verse: Praise Him with timbrel and dance, * praise him with strings and
                flute.
                With our voices let us shout * and magnify the Precious Cross in hymns; *
                let us kiss it with adoration and cry aloud: * O all-honored Cross, sanctify our
                souls and bodies by thy power, * and keep unharmed from all malice of the
                enemy ** those who venerate thee with sincere reverence.
                Verse: Praise Him with tuneful cymbals, praise Him with cymbals of
                jubilation. * Let every breath praise the Lord.
                Approach and draw from the never-failing waters * pouring forth with grace
                from the Cross. * Behold! ye see the holy Wood set before you, the source of
                divine gifts, * upon which there flowed blood and water from the wounded side
                of the Lord of all. * and upon which He was willingly raised ** raising up mortal
                mankind.
                Verse: Exalt ye the Lord our God: * And worship at His footstool, for
                He is holy.
                O all-honored Cross, thou art the firm foundation of the Church, * the glory
                and salvation of monastics. * Venerating thee today, we are filled with light in
                heart and soul, * by the divine grace of the Lord, Who was nailed upon thee *
                overthrowing the power of the deceitful one, ** and annulling the curse.
                Verse: God is our King before the ages: * He hath wrought salvation in
                the midst of the earth.
                With our voices let us shout * and magnify in songs the precious Cross; * let
                us kiss it with adoration and cry aloud: * O all-honored Cross, sanctify our souls
                and bodies by thy power, * and keep unharmed from all malice of the enemy **
                those who venerate thee with sincere reverence.
                Verse: Arise, O Lord my God, let Thy hands be lifted on high; * forget
                not Thy paupers to the end.
                Tone VIII: The Lord of all hath taught us in a parable * to shun the boastful
                thoughts of the evil Pharisees; * and instructed us all to not think more highly of
                ourselves than we should. * He Himself became our pattern and example, * for
                He emptied Himself even unto death upon the Cross. * Let us therefore render
                thanks with the Publican and say: * O God Who hast suffered for us and yet
                remained impassible, ** deliver us from the passions and save our souls.
            """
            ,'aposticha_theotokion': """
                Glory ..., Sticheron from the Triodion, in Tone VIII:
                The Lord of all hath taught us in a parable * to shun the boastful thoughts
                of the evil Pharisees; * and He hath instructed us all to not think more highly of
                ourselves than we should. * He Himself became our pattern and example, * for
                He emptied Himself even unto death upon the Cross. * Let us therefore render
                thanks with the Publican and say: * O God Who hast suffered for us and yet
                remained impassible, ** deliver us from the passions and save our souls.
                Now & ever ..., in Tone II:
                Most Blessed art Thou, O Virgin Theotokos, * for through Him Who
                became incarnate of thee is Hades led captive, * Adam recalled, the curse
                annulled, Eve set free, death slain, * and we are given life. Wherefore, we cry
                aloud in praise: * Blessed art Thou, O Christ God, * Who hast been thus wellpleased, glory to Thee.
            """
            ,'apolytichia':"""
                In Tone II: Come, ye faithful, and let us venerate the life-giving Tree, *
                upon which Christ, the King of Glory, hath willingly stretched out His hands. *
                To the ancient blessedness hath He raised us up, * whom the enemy despoiled of
                old through pleasure, making us exiles far from God. * Come, ye faithful, and let
                us venerate the Tree * whereby we have been deemed worthy to crush the heads
                of our invisible enemies. * Come, all ye kindred of the nations, * and let us honor
                in hymns the Cross of the Lord. * Rejoice, O Cross, perfect redemption of fallen
                Adam. * Glorying in thee, our faithful kings by thy might laid low the people of
                Ishmael. * We Christians kiss thee now with awe, * and glorifying God Who was
                nailed on thee, we cry aloud: * O Lord, Who was crucified on the Cross, have
                mercy on us, ** for Thou art good and the Lover of mankind.
                In Tone VIII: Today the Master of creation and the Lord of Glory * hath
                been nailed to the Cross, His side pierced with a lance; * and He Who is the
                sweetness of the Church tasteth gall and vinegar. * A crown of thorns hath been
                placed upon Him, * He Who covereth the heavens with clouds hath been
                clothed in a cloak of mockery, * and He Who formed man with His hands hath
                been struck by a hand of clay. * He Who doth wrap the heaven in clouds hath
                been smitten upon His back. * He accepteth spitting and scourging, reproach
                and buffeting; * and all these things my Redeemer and God endured for me who
                am condemned, ** that in His compassion He may save the world from
                delusion.
                Glory ..., in Tone VIII:
                Today He Who is in essence unapproachable, * hath become approachable
                for me * and suffereth His Passion, delivering me from the passions. * He Who
                granteth light unto the blind * hath been spat upon by the mouths of
                transgressors, * giving His back over to scourging * for the sake of those held
                captive. * When the pure Virgin, His Mother saw Him upon the Cross, * she
                cried aloud in pain: * “Woe is me, my Child! What is this that Thou hast done? *
                Thou Who wast in beauty fairer than all mortal men, * dost now appear without
                life and form, * having neither shape nor comeliness. * Woe is me, my Light! * I
                cannot bear to look upon Thee sleeping, * and I am wounded in the depths of
                my soul, * a harsh sword hath pierced my heart. * I sing the praises of Thy
                Passion, * I venerate Thy loving-kindness: ** O long-suffering One, glory be to
                Thee!
                Now & ever ..., in Tone VI:
                Today the words of the Prophet have been fulfilled: * For behold, we
                worship at the place upon which Thy feet have stood, O Lord; * and tasting
                from the Tree of salvation, * we have been delivered from our sinful passions *
                by the intercessions of the Theotokos, ** O Thou Who alone lovest mankind
            """
        } #Matins
        ,'liturgy': {
            'beatitudes': [
                """
                    Thou didst arise O Christ, and trample upon death as a King almighty;
                    Thou didst recall us from the vaults of Hades to the enjoyment of the Kingdom
                    of Heaven, in the land of immortality.
                """
                ,"""
                    O ye faithful, let us cry aloud with divine songs, chanting triumphantly to
                    God, as we kiss the Cross of the Lord; for it is a fount of holiness to all those in
                    this world.
                """
                ,"""
                    Glory ..., I praise the Unity in three Hypostases and the Trinity worshipped
                    in one Nature, the Triune God, three-sunned Light, the Father, Son and Holy
                    Spirit.
                """
                ,"""
                    Now & Ever ..., O undefiled Ewe-lamb, a wonder greater than all wonders
                    hath been revealed in thee: For thou hast borne the Lamb that taketh away the
                    sins of the world, fervently entreat Him on behalf of those who sing thy praises.
                """
            ]
            ,'troparion':"""
                Troparion of the Cross in Tone I:
                Save O lord Thy people * and bless thine inheritance. * Grant now unto the
                faithful, * victory over adversaries, * and by the power of Thy Cross * do Thou
                preserve Thy commonwealth.
            """
            ,'kontakion': """
                Kontakion of the Cross in Tone VII:
                The fiery sword no longer guardeth the gates of Eden, * for it hath been
                wondrously quenched by the wood of the Cross. * The sting of death and the
                victory of Hades have been vanquished, * for Thou art come, O my Savior,
                crying unto those in Hades: ** “Enter again into Paradise.”
            """
            ,'prokeimenon':"""
                Prokeimenon for the Cross in Tone VI: Save O Lord Thy people, * and
                bless Thine inheritance.
                The Verse: Unto Thee, O Lord, will I cry; O my God, be not silent
                unto me.
            """
            ,'readings': """
                EPISTLE TO THE HEBREWS (4:15 - 5:6)
                Brethren: Seeing then that we have a great high priest, that is passed into the
                heavens, Jesus the Son of God, let us hold fast our profession. For we have not
                an high priest which cannot be touched with the feeling of our infirmities; but
                was in all points tempted like as we are, yet without sin. Let us therefore come
                boldly unto the throne of grace, that we may obtain mercy, and find grace to help
                in time of need. For every high priest taken from among men is ordained for
                men in things pertaining to God, that he may offer both gifts and sacrifices for
                sins: Who can have compassion on the ignorant, and on them that are out of the
                way; for that he himself also is compassed with infirmity. And by reason hereof
                he ought, as for the people, so also for himself, to offer for sins. And no man
                taketh this honour unto himself, but he that is called of God, as was Aaron. So
                also Christ glorified not himself to be made an high priest; but he that said unto
                him, Thou art my Son, to day have I begotten thee. As he saith also in another
                place, Thou art a priest for ever after the order of Melchisedec.
                Alleluia from the Triodion, in Tone II:
                Verse: Remember Thy congregation which Thou hast purchased from
                the beginning.
                Verse: But God is our King before the ages: He hath wrought salvation
                in the midst of the earth
                GOSPEL ACCORDING TO ST. MARK (8:34-9:1)
                At that time: when Jesus had called the people unto him with his disciples
                also, he said unto them, Whosoever will come after me, let him deny himself, and
                take up his cross, and follow me. For whosoever will save his life shall lose it; but
                whosoever shall lose his life for my sake and the gospel’s, the same shall save it.
                For what shall it profit a man, if he shall gain the whole world, and lose his own
                soul? Or what shall a man give in exchange for his soul? Whosoever therefore
                shall be ashamed of me and of my words in this adulterous and sinful generation;
                of him also shall the Son of man be ashamed, when he cometh in the glory of his
                Father with the holy angels. And he said unto them, Verily I say unto you, That
                there be some of them that stand here, which shall not taste of death, till they
                have seen the kingdom of God come with power.
            """
        } #Liturgy
    } #Service
    ,'-21': { #4th Sunday | St John of the Ladder
        'vespers': {
            'stichera_tone': 'in Tone VIII; Spec. Mel.: “O most glorious wonder ...”:'
            ,'stichera': [
                """
                    O holy father John, * truly didst thou carry upon thy lips the praises of God,
                    * having studied with exceeding diligence * the divinely inspired Scriptures O allwise one * thou didst enrich thyself with the gifts of grace, * and become a
                    blessed one, ** vanquishing all the counsels of the ungodly.
                """
                ,"""
                    O most glorious father John, * thou didst cleanse thy soul with the fountain
                    of thy tears, * and through the keeping of all-night vigil * thou didst gain God’s
                    mercy, * raising thyself on high O blessed one, * to the love of Him and of His
                    beauty; * and as is meet thou dost take delight and ever rejoice, * with thy fellow
                    strugglers, ** O divinely wise father.
                """
                ,"""
                    O venerable father John, * through faith thou didst lift up thy mind on high
                    to God; * dead to the never-waning turmoil of this world, * thou didst take up
                    thy Cross and follow Him, * Who seeth all things, * bringing into subjection *
                    the unruliness of thy body * through ascetic discipline, ** by the power of the
                    Divine Spirit.
                """
            ]
            ,'doxastichon': """
                in Tone V:
                O holy father, hearing the voice of the Gospel of the Lord, * and having
                forsaken the riches and glory of this world; * thou didst cry out unto all: * “Love
                God, and ye shall find eternal grace, * esteem nothing higher than His love, *
                that, when He cometh in His glory, * ye may find rest with all the saints.” ** by
                whose prayers, O Christ, do Thou protect and save our souls.
            """
            ,'aposticha_theotokion': """
                Glory to the Saint..., in Tone II:
                Let us offer honor unto John, * an angel upon the earth and a man of God
                in the heavens, * adornment of the whole world, * joy of the good and boast of
                virtuous ascetics. * For planted in the house of God * he hath blossomed forth
                with holiness, * and like a cedar in the desert * he hath increased the flock of
                Christ ** in ascetic sanctity and righteousness.
                Now & ever ..., in Tone II:
                O new wonder greater than all the wonders of old! * For who hath ever
                known a mother to give birth without having known a man, * and to bear on her
                arm Him Who sustaineth all creation? * Yet it was the will of God to be born. *
                O most pure one, who carried Him as an infant in Thine embrace * and before
                Whom thou hast a mother’s boldness: * cease not to pray on behalf of those
                who honor thee, ** that He have compassion and save our souls.
            """
        } #Vespers
        ,'matins': {
            'troparion': """
                Glory ..., Troparion of St. John Climacus in Tone I:
                A dweller in the wilderness and an angel in the body! * Thou wast manifest a
                wonderworker, O John our Godbearing Father! * Thou didst receive heavenly
                gifts through fasting, vigil, and prayer: * healing the infirm and the souls of those
                who flee to thee with faith. * Glory to Him Who hath given thee strength! *
                Glory to Him Who hath crowned thee! ** Glory to Him Who through thee
                worketh healings for all!
                Now & ever ..., in Tone I:
                When Gabriel announced to thee, “Rejoice!”, O Virgin, * the Master of all
                became incarnate within thee, the holy tabernacle, * at his cry, as the righteous
                David said. Thou wast shown to be more spacious than the heavens, * having
                borne thy Creator. * Glory to Him Who made His abode within thee! * Glory to
                Him Who came forth from thee! ** Glory to Him Who hath set us free by thy
                birthgiving.
            """
            ,'after50': """
                in Tone VIII:
                Glory ..., The gates of repentance, do Thou open unto me, O Giver of Life, * for
                early in the morning my spirit seeketh Thy holy temple, * bearing the temple of
                my body all defiled. * But as One who art compassionate * cleanse it by Thy
                loving-kindness and mercy.
                Now & ever ..., Guide me on the paths of salvation, O Theotokos: * for I have
                polluted my soul with shameful deeds * and wasted all my life in slothfulness. *
                but by thine intercessions * do thou deliver me from all impurity.
                In Tone VI:
                Have mercy upon me, O God, * according to Thy great mercy: * and according
                to the multitude of Thy compassion * blot out my transgressions.
                In Tone VIII: As I the wretched one ponder the multitude of evil deeds I have
                done, * I tremble for fear of the dread day of judgment. * But trusting in Thy
                compassionate mercy, * like David do I cry unto Thee: * “Have mercy upon me,
                O God, according to Thy great mercy”.
            """
            ,'canon': """
                ODE I
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion, in Tone V:
                Irmos: Unto God the Savior ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                O Christ, I have become like the man who fell among thieves, and
                grievously beaten, was left barely alive O Savior; and more than he, I am also
                grievously wounded with my sins.
                Refrain: Have mercy on me, O God, have mercy on me.
                Stripped of all Thy wealth, he cried out lamenting: “O Savior, I am gravely
                wounded; leave me not to the thieves.” Likewise I also pray to Thee: “Merciful
                Lord, save me”.
                Refrain: Have mercy on me, O God, have mercy on me.
                Do Thou heal me who am noetically deadened by the scourging of sin, from
                the unrighteous thieves, my wicked thoughts, O Christ Savior; save me since
                Thou art plenteous in mercy.
                Refrain: Most Holy Theotokos save us.
                Theotokion: O thou who didst inexplicably give birth to the Wisdom and
                Word of the Father, grant healing to my grievously wounded soul, and assuage
                the infirmity of my heart.
                Of Saint John, in Tone VI
                Irmos: Having passed through the water as upon dry land ...,
                Refrain: Venerable father John, Pray to God for us.
                Ascending from the sorrow of things material, O holy John, thou didst dwell
                in the immaterial noetic light: by thine intercessions to the Lord, grant me this
                light.
                Refrain: Venerable father John, Pray to God for us.
                Suckled on the sweetness of abstinence, thou didst cast away the bitterness
                of sensuality; and so, father, thou hast granted us a pleasure sweeter than honey
                and the honeycomb.
                Glory..., Having ascended to the heights of the virtues, scorning as
                worthless, sensual pleasures, thou hast appeared to thy flock as the sweetness of
                salvation, O venerable father.
                Both...: O thou who ineffably gave birth to the Word and Wisdom of the
                Father, heal thou the harsh wounds of my soul and assuage the infirmity of my
                heart.
                Katavasia in Tone IV: I shall open my mouth, * and be filled with the
                Spirit, * and utter discourse to the Queen and Mother; * and be seen
                radiantly keeping festival, * joyfully praising her wonders.
                ODE III
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion, in Tone V:
                Irmos: Do Thou establish us O God our Savior ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I have wickedly journeyed on the path of life, O Christ, and been sorely
                wounded by thieves through my passions: but I beseech Thee, raise me up.
                Refrain: Have mercy on me, O God, have mercy on me.
                Thieves have robbed my mind and, wounded by my sins, leaving me barely
                alive: but do Thou heal me, O Lord.
                Refrain: Have mercy on me, O God, have mercy on me.
                I have been stripped bare of Thy commandments by the passions O Christ
                Savior, and I have been scourged by sensual pleasures, but do Thou pour upon
                me Thy mercy.
                Refrain: Most Holy Theotokos save us.
                Theotokion: Without ceasing Pray, O pure one, unto Him who came forth
                from thy womb, that those who sing thy praises may be delivered from the wiles
                of the evil one.
                Of Saint John, in Tone VI
                Irmos: Thou art the strengthening of all who come to Thee ...,
                Refrain: Venerable father John, Pray to God for us.
                With the fiery coal of thine asceticism, O saint, thou hast burnt up the
                thorns of the passions, warming all those who follow the monastic life.
                Refrain: Venerable father John, Pray to God for us.
                The aroma of the sanctifying myrrh of thine ascetic struggles, O venerable
                father, Hath filled all with the odor of the spiritual fragrance of God.
                Glory..., Attentively learning the laws of ascetic struggle, thou didst burn up
                the passions, as though another army of Pharaoh, by the flow of thy tears.
                Both...: Do thou put a stop the restless tumult of my thoughts, O pure one,
                and guide me, O Mother of God, to thy Son.
                Katavasia: O Theotokos, thou living and plentiful fount, * establish in
                spiritual fellowship those who sing hymns to thee, * and in thy divine
                glory * grant them crowns of glory.
                Kontakion of the Saint in Tone IV:
                Truly hath the Lord placed thee * in the firmament * like an immovable star
                of abstinence * shedding its light upon all creation, ** O father John our teacher.
                Ikos: Truly, O father, thou hast made thyself into a temple of God, adorned
                through thy divine virtues with faith, hope and true love, as if with gold shining
                from afar; thou hast explained the laws of God, and practiced abstinence as a if a
                bodiless one; having acquired wisdom, courage, chastity and humility, thou hast
                been raised on high, illumined with unceasing prayer, thou hast attained unto the
                tabernacles of heaven, O father John our teacher.
                Sessional hymn, in Tone V:
                Having Thy Most-pure Cross as a weapon of salvation, O Savior, we cry to
                Thee: “O Thou Who willingly didst suffer for our sake, save us, O God of all,
                since Thou art plenteous in mercy”.
                Sessional hymn of the Saint, in Tone IV:
                Glory ..., Having ascended to the Heavens, resplendent with virtues and
                holiness, thou hast properly entered into the boundless depth of the
                contemplation of God. Having defeated all the snares of the demons, and
                protecting mankind from their wickedness, O John - ladder of the virtues - thou
                dost ever intercede on behalf of thy servants, that they be saved.
                Now & Ever..., He Who is enthroned upon the cherubim and Who
                dwelleth in the bosom of the Father, hath sat incarnate in thy bosom, O Lady, as
                upon His holy throne. For as God He is the ruler of all nations, and with
                understanding we now sing unto Him; beseech Him O pure one, on behalf of
                thy servants that they be saved.
                ODE IV
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion, in Tone V:
                Irmos: I heard the rumor of Thy plan ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                Thieves have despoiled me of my godly actions and left me wounded and in
                pangs.
                Refrain: Have mercy on me, O God, have mercy on me.
                My unstable thoughts have stripped me bare of Thy commandments, O
                Savior, and I have been scourged by my transgressions.
                Refrain: Have mercy on me, O God, have mercy on me.
                The Levite, when he saw me wounded, passed me by, O Savior; but do
                Thou save me.
                Refrain: Most Holy Theotokos save us.
                Theotokion: Regally do we glorify thee O unwedded Theotokos, and we the
                faithful flee to thy safe haven for refuge.
                Of Saint John, in Tone VI
                Irmos: I have heard, O Lord, the mystery of Thy plan ...,
                Refrain: Venerable father John, Pray to God for us.
                Thou art a fragrant flowered meadow and a living paradise of the virtues, in
                which abstinence doth blossom; and with which thou dost nourish all who honor
                thee.
                Refrain: Venerable father John, Pray to God for us.
                As a lawgiver for ascetics, and a most meek rule for monastics, thou art truly
                like Moses and David, O father, wherefore we bless thee.
                Glory..., Planted by the waters of abstinence, thou hast been revealed O
                blessed one, to be a vine blossoming with, and bearing, the grapes of piety.
                Now & ever ..., Within time, O Mother of God, thou didst bear for us Him
                Who hath shone forth timelessly from the Father. Entreat Him to save those
                who sing thy praises.
                Katavasia: He who sitteth in glory upon the throne of the Godhead, *
                Jesus the true God, * is come in a swift cloud * and with His sinless hands
                he hath saved those who cry: * Glory to Thy power, O Christ.
                ODE V
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion, in Tone V:
                Irmos: Having arisen early I cry unto Thee O Lord ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                O Jesus, bind the wounds of my soul, as of old the Samaritan did to him
                that fell among thieves, and heal me from my pain, I pray Thee, O my Christ.
                Refrain: Have mercy on me, O God, have mercy on me.
                Sickened by the wounds of my transgressions, I lay helpless, O my Christ,
                naked and bereft of the divine virtues; but I beseech Thee, do Thou save me.
                Refrain: Have mercy on me, O God, have mercy on me.
                When the priest and the Levite saw me, they could not help me, but passed
                by on the other side. But since Thou art compassionate Thou hast granted me
                salvation and saved me.
                Refrain: Most Holy Theotokos save us.
                Theotokion: I beseech Thee O Lord, Turn not away from me, wretched as I
                am, for my mind is painfully scourged by noetic thieves, but do Thou have
                compassion upon me O Savior, by the prayers of her who gave birth to Thee.
                Of Saint John, in Tone VI
                Irmos: A strange darkness hath overcome me ...,
                Refrain: Venerable father John, Pray to God for us.
                O blessed father, thou didst quench all the passions with the dew of thine
                ascetic struggles, abundantly aflame with love and faith thou wast a lamp of
                abstinence, a light of dispassion, and a child of the day.
                Refrain: Venerable father John, Pray to God for us.
                With thy divine husbandry, O father, thou didst tend to the grapes of faith;
                and gathering them into the winepress thou hast pressed them out by thine
                ascetic labors; making glad the heart of thy flock.
                Glory..., Having well withstood the assaults and the wounds of thine
                enemies, thou wast revealed to be a pillar of patience, strengthening thy flock
                thou hast guided them with thy blessed staff, nourishing them on the waters of
                abstinence, O blessed one.
                Now & ever ..., As spoken by thine own lips, we emulate thee, O all-pure
                one, and call thee blessed. For the Lord hath indeed done great things unto thee
                and hath magnified thee as the true Mother of God, born from thy womb.
                Katavasia: All creation stands in awe of thy divine glory; * for thou, O
                Virgin who hast not known wedlock, * didst contain within thy womb the
                God of all, * and gave birth to the timeless Son, * bestowing peace, upon
                all who hymn thee.
                ODE VI
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion, in Tone V:
                Irmos: An Abyss hath consumed me ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I have wasted the blessed life given me with passions, O Master, and
                grievously scourged in every part by my transgressions, I turn back to Thee for
                refuge and pray: “Have compassion upon me”.
                Refrain: Have mercy on me, O God, have mercy on me.
                Thieves have seized my wealth and left me as one dead, having scourged my
                mind with the passions. But do Thou have compassion upon me and save me, O
                Lord.
                Refrain: Have mercy on me, O God, have mercy on me.
                Unable to bear the sight of my pain and wounds, the Levite passed me by;
                but do Thou Thyself O Compassionate One, pour on me the oil of Thy great
                mercy.
                Refrain: Most Holy Theotokos save us.
                Theotokion: As the bush unconsumed by fire, as the mountain and living
                ladder, as the heavenly gate, we worthily glorify thee, Mary most glorious, the
                praise of the Orthodox.
                Of Saint John, in Tone VI
                Irmos: Cleanse me, O Savior ...,
                Refrain: Venerable father John, Pray to God for us.
                Thou didst receive within thy soul the divine wealth of the Spirit;
                unblemished prayer, purity, modesty, constant watchfulness, the labors of
                abstinence; by which thou hast become a temple of God.
                Refrain: Venerable father John, Pray to God for us.
                O wise one, thou didst pass by material things as worthless, and having
                raised thy mind on high through noetic prayer; by the perfection of thy life thou
                hast manifest thyself as an heir of peaceful repose in the highest.
                Glory..., Thou didst truly extinguish the fiery darts of thine enemies by thine
                ascetic struggles, and having kindled the fire of faith, thou didst burn up the
                boastful unbelief of heresy.
                Both...: The majesty of the Most High hath shone forth from Zion; through
                an ineffable union He hath assumed flesh from thee, O undefiled one, and shed
                light upon the world.
                Katavasia: Celebrating the divine and solemn feast * of the Mother of God
                * O ye divinely wise, * let us come, clapping our hands, * and glorify God
                who was born of her.
                SYNAXARION READING
                Verse: Thou dwellest no longer at thine earthly diocese O John,
                Verse: But thou dost always delight in the vision of Him Who overseeth all.
                On this day, the fourth Sunday of Great Lent, we commemorate our
                venerable Father among the saints, St. John of Sinai, the author of The Ladder of
                Divine Ascent.
                No one knows the birthplace or parentage of our venerable Father John of
                Sinai. In his youth, at the age of sixteen, he came to the wilderness of Sinai and
                dwelt under the guidance of Abba Martyrius. When Abba Martyrius tonsured our
                venerable Father John at the age of twenty, he took him and went to that pillar
                of the wilderness, Abba John the Sabbaite in the wilderness of Gouda where he
                had with him his disciple Stephen the Cappadocian. When the Sabbaite elder saw
                them, he arose and took water, poured it into a small basin, washed the feet of
                the disciple (the young John) and kissed his hand; but he did not wash the feet of
                Abba Martyrius his superior. Abba Stephen was scandalized by the situation.
                After the departure of Abba Martyrius and his disciple, Abba John noticed that
                his own disciple was greatly perplexed and said to him, “Why are you so
                troubled? Believe me, I do not know who the boy is, but today I received the
                abbot of Sinai and washed his feet.” After forty years, he did indeed become the
                abbot according to the prophecy of the elder. After the passing of his spiritual
                father, St. John continued alone in the wilderness in a cave in Wadi-Thola. He
                traveled from time to time, going at least once as far as Alexandria. He records
                in The Ladder his visit to a large monastic community there and the marvels of
                repentance, obedience, and humility which he observed. In his humility, he
                counted our venerable George the Wonderworker of Arselaou as his master. In
                all, he spent some forty years in solitude and stillness. He guided the monks who
                dwelt in that desert since he was a most excellent and nurturing spiritual father –
                for in those days there were innumerable ascetics living in cells all through the
                mountains and valleys of Sinai. From time to time, he received visitors froih
                farther away. At one point, some other monks, prompted to jealousy by the
                adversary who hates all good, complained of Abba John’s fame and teaching. In
                response, he humbly kept strict silence for over a year, until the same fathers
                who had complained came, asking him to speak again for the benefit of all. After
                he had spent forty years in the wilderness, the monks of Sinai asked him to
                become abbot of the great monastery built by the emperor Justinian beside the
                Burning Bush of Moses, the Holy Monastery of St. Catherine. In obedience to
                the fathers, he left his blessed solitude to take up the responsibilities of abbot. It
                is told that on the very day on which he assumed the office of abbot, there came
                a group of about six hundred pilgrims. When they were seated, our venerable
                Father John saw someone in the crowd with short hair and wearing a Jewish
                tunic. This person was going about like someone with authority, directing the
                cooks, the stewards, the storekeepers, and other workers. After the people left,
                when the servers all sat down to eat, they sought everywhere for the one who
                had been going about supervising, but did not find him. Then the servant of
                God, our venerable Father John, said, “Let him go. The lord Moses did nothing
                strange in this same place where he served before and which belongs to him.” O,
                the wonder! It had been the Holy Prophet and Lawgiver Moses who had served
                the guests. At the request of Abba John, abbot of Raith near the shore of the
                Red Sea, our venerable father wrote his wonderful book, The Ladder of Divine
                Ascent, in which he sets out the whole of Christian life as a divine ascent of thirty
                rungs to Christ. This book has been a treasure, a pearl beyond price, to this day.
                It is useful not only to monastics but to all devout Christians. He also wrote, for
                Abba John, a shorter exhortation, “To the Shepherd,” in which he set out the
                stature and work of the father and shepherd of souls who must guide, not so
                much by words but by the light of holiness in which he lives. St. John was a true
                physician of souls and had great spiritual insight into men's behavior. He made
                detailed observations of the symptoms of men's sin-sick souls, diagnosed their
                spiritual diseases, and prescribed the appropriate medicine for their recovery and
                salvation. He showed how one can ascend the “ladder of the virtues” step by
                step and reach the Promised Land, fleeing the Egypt of the passions. Yet, his
                success was due only to his own life of constant watchfulness, fasting, vigils, and
                prayer. The monastic community he shepherded continues to this day beside the
                Burning Bush, and his teachings guide and direct monastics throughout the
                world. During Great Lent, The Ladder is read aloud in monasteries during meals
                so the monastics may receive his edifying spiritual counsels for their souls’
                sustenance, as they simultaneously receive physical nourishment for their bodies.
                Today, the cave in which he dwelt in the wilderness of Sinai i can still be seen,
                but his resting place is unknown except to the angels. He fell asleep in the Lord
                in the seventh century. St. John is also commemorated on March 30, the day of
                his repose.
                О Christ our God, through the intercessions
                of our venerable Father John of The Ladder,
                have mercy on us and save us. Amen.
                ODE VII
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion, in Tone V:
                Irmos: The highly exalted Lord of our fathers ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                Thieves fell upon me, wretch that I am, and left me with wounds as one
                dead; wherefore I pray unto Thee: O God come Thyself and visit me.
                Refrain: Have mercy on me, O God, have mercy on me.
                My mind, ceaselessly robbed by my thoughts, hath pierced me through with
                the passions, and because of the multitude of my transgressions, left me as one
                dead. But do Thou O Savior, grant me healing.
                Refrain: Have mercy on me, O God, have mercy on me.
                Having seen me ailing with painful wounds, the Levite could not bear to
                look upon me, thinking my wounds incurable, and passed me by O my Savior,
                but do Thou Thyself grant me healing
                Refrain: Most Holy Theotokos save us.
                Theotokion: Having taken flesh from the Virgin, Thou hast saved me, in
                Thy compassion pouring upon my wounds Thy rich mercy, O Christ, wherefore
                I glorify Thee.
                Of Saint John, in Tone VI
                Irmos: Having gone down to Babylon from Judea ...,
                Refrain: Venerable father John, Pray to God for us.
                Into the fair meadows of the Kingdom on high, Thou hast lead thy flock to
                pasture, O father, and with the rod of true dogma thou hast driven away the wild
                beasts of heresy; chanting: “O God of our fathers, blessed art Thou”.
                Refrain: Venerable father John, Pray to God for us.
                Thou hast entered on high, into the heavenly bridal chamber of Christ the
                King, clothed in a garment worthy of Him that hath called thee; and seated
                therein, thou dost cry aloud: “O God of our fathers, blessed art Thou”.
                Glory..., Thou art a river of abstinence unpolluted by sin O father; purging
                the thoughts and cleansing the filth of those, who sing with faith, “O God of our
                fathers, blessed art Thou”.
                Both...: The Lord of all came forth from thy womb, taking flesh from thee,
                O Virgin. Wherefore with true Orthodox faith we honor thee as the Theotokos,
                and cry aloud to thy Son: “O God of our fathers, blessed art Thou”.
                Katavasia: Refusing to worship created things * in place of the Creator, *
                the divinely wise youths bravely trampled down the threatening fire * and
                rejoicing they sang aloud: * O supremely hymned Lord and God of our
                Fathers, Blessed art Thou.
                The Kontakion and Ikos of the Resurrection in the Tone of the week.
                ODE VIII
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion, in Tone V:
                Irmos: The Youths in the fiery furnace ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                From the noetic thieves of my thoughts, O Savior, I have been robbed, and
                from the wounds of my transgressions, my life hath wasted away, from whence I
                have been stripped of the divine image of Thee O God, who art the Lover of
                mankind, but do Thou have compassion upon me.
                Refrain: Have mercy on me, O God, have mercy on me.
                Thou didst come down from on high to the earth, O Savior, and have
                compassion upon me, and as I lay wholly wounded by the scourging of sin O
                Compassionate One; Thou hast poured the oil of Thy mercy upon me, O Christ.
                Refrain: Have mercy on me, O God, have mercy on me.
                For my sake, O Master and Savior, Thou hast given Thy soul and body over
                to deliver me, and save me, who lay incurably wounded by the sword of my sins,
                since Thou art Compassionate.
                Refrain: Most Holy Theotokos save us.
                Theotokion: Transcending all understanding hast thou given birth to the
                Lord, God-man and Word, yet remaining a virgin; wherefore, O Virgin, with all
                creation we bless and supremely exalt thee throughout all ages.
                Of Saint John, in Tone VI
                Irmos: The King of glory ...,
                Refrain: Venerable father John, Pray to God for us.
                An image and living pillar of abstinence art thou shown to be in truth O
                father, wherefore we honor thy memory O John.
                Refrain: Venerable father John, Pray to God for us.
                The multitudes of monastics rejoice, and the assembly of venerable saints
                and righteous dance with gladness: for thou hast justly received a crown with
                them.
                Refrain: Let us bless Father, Son, Holy Spirit, the Lord.
                Adorned with the virtues, thou hast entered into the ineffable glory of the
                noetic bridle-chamber singing hymns in praise of Christ throughout the ages.
                Now & Ever ..., Reject us not, O Virgin, for we are in need of thy help; and
                we sing in praise of thee and supremely exalt thee throughout all ages.
                Stichera: We praise, bless and worship the Lord, chanting and
                supremely exalting Him throughout all ages.
                Katavasia: The Offspring of the Theotokos * saved the holy children in the
                furnace. * He who was then prefigured hath now been born on earth, *
                and He gathereth all creation to hymn thee: * all ye works praise ye the
                Lord * and supremely exalt Him throughout all ages.
                And then we chant the Hymn of the Most Holy Theotokos (the Magnificat)
                ODE IX
                The appointed Canons from the Oktoechos. Then:
                The first Canon from the Triodion, in Tone V:
                Irmos: O Isaiah, dance now and be glad! ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I have knowingly not kept Thy commandments O Lord, and following the
                passionate impulses of sensual pleasure, I have been stripped of grace, and cast
                out naked. Wherefore I beseech Thee O Savior, do Thou save me
                Refrain: Have mercy on me, O God, have mercy on me.
                The Levite could not cleanse my wounds, but as one who hath suffered with
                me, Thou didst come to me O good One, and pouring upon me the mercy of
                Thy compassions; like the best of physicians, Thou hast healed me.
                Refrain: Have mercy on me, O God, have mercy on me.
                Since Thou art the compassionate One, Thou hast been compassionate to
                me O Christ, and saved me, who wast grievously wounded by thieves O Savior;
                by giving Thy soul and body as the two dinars, in payment for my redemption.
                Refrain: Most Holy Theotokos save us.
                Theotokion: Thy birth-giving transcends understanding, O Mother of God,
                for thou didst conceive without knowing a man, and gave birth while remaining a
                virgin, having given birth to God, Whom magnifying, we call thee blessed, O
                Virgin.
                Of Saint John, in Tone VI
                Irmos: With all peoples let us magnify the Pure One ...,
                Refrain: Venerable father John, Pray to God for us.
                A physician of those sick through sin, O blessed one of God, thou art
                manifest as a slayer and expeller of evil spirits; wherefore we call thee blessed.
                Refrain: Venerable father John, Pray to God for us.
                Leaving the earth wherein corruption dwelleth, thou hast gone to live, O
                father, in the land of the meek, and with them thou dost rejoice in the sweet
                blessings of God.
                Glory..., Today is the day of solemn festivity, for the entire flock of
                monastics hath been called to assemble as a spiritual choir, and liturgizing,
                partake of eternal life.
                Both...: Having taken up His abode within thee, O all-immaculate One, He
                who hath overthrown the murderer who maliciously brought about the fall of
                our first parents, hath been born and saved us all.
                Katavasia: Let every mortal born on earth, * radiant with light, in spirit
                leap for joy; * and let the host of the angelic powers * celebrate and honor
                the holy feast of the Mother of God, * and let them cry aloud: * Rejoice! O
                Theotokos, thou pure Ever-Virgin.
            """
            ,'exapostilarion': """
                Glory ..., Exapostilarion from the Triodion, in Tone III;
                Thou didst shun worldly ease as enfeebling, * and withering thy flesh with
                fasting, * thou didst renew the strength of thy soul, O venerable one, * gloriously
                enriching thyself with heavenly glory, ** wherefore cease not to intercede on our
                behalf, O John.
                Now & ever ..., in the same Tone;
                Saved by thee, O Lady, we nobly confess Thee to be the very Theotokos, *
                for inexpressibly Thou didst bear God, * Who hath destroyed death by the Cross
                * and called to Himself the assemblies of venerable saints, ** wherefore we, with
                them, offer praises to Thee, O Virgin.
            """
            ,'aposticha': """
                from the Triodion, in Tone I:
                9th Verse: Arise, O Lord my God, let Thy hands be lifted high; * forget
                not Thy paupers to the end.
                Come, let us work in the mystical vineyard, * bringing forth fruits of
                repentance therein; * let us not labor for the sake of food and drink, * but
                through prayer and fasting let us increase the virtues. * And the Lord of the
                vineyard, pleased by our labor, will pay us the dinar, * with which He hath
                redeemed our souls from the debt of sin, ** for He alone is rich in mercy.
            """
            ,'aposticha_theotokion': """
                Glory ..., in Tone I:
                Come, let us work in the mystical vineyard, * making the fruit of repentance
                grow within it; * let us not labor for the sake of food and drink, * but through
                prayer and fasting let us gain the virtues. * And the Lord of the vineyard, pleased
                by our labor, will provide the payment, * whereby He doth redeem our souls
                from the debt of sin, ** for He alone is abundantly merciful.
                Now & ever ..., Theotokion, in Tone II:
                Thou art most blessed, O Virgin Theotokos, * for through Him who took
                flesh from thee, Hades hath been captured, * Adam recalled, the curse slain, Eve
                set free, * death put to death, and we have been given life. * Therefore in praise
                we cry: ** Blessed art thou, O Christ our God, who hast been thus well-pleased,
                glory be to thee.
            """
        } #Matins
        ,'liturgy': {
            'troparion':"""
                Troparion of the Saint, in Tone I:
                A dweller in the wilderness and an angel in the body! * Thou wast manifest a
                wonderworker, O John our Godbearing Father! * Thou didst receive heavenly
                gifts through fasting, vigil, and prayer: * healing the infirm and the souls of those
                who flee to thee with faith. * Glory to Him Who hath given thee strength! *
                Glory to Him Who hath crowned thee! ** Glory to Him Who through thee
                worketh healings for all!
            """
            ,'kontakion': """
                Glory ..., Kontakion of the Saint, in Tone IV:
                Truly hath the Lord placed thee * in the firmament * like an immovable star
                of abstinence * shedding its light upon all creation, ** O father John our teacher.
                Now & Ever ..., in Tone VI:
                O protection of Christians that cannot be put to shame, * O mediation unto
                the Creator unfailing, * disdain not the suppliant voices of sinners, * but be thou
                quick, O good one, to help us who in faith cry unto thee; * hasten to intercession
                and speed thou to make supplication, ** thou who dost ever protect, O
                Theotokos, them that honor thee.
            """
            ,'prokeimenon':"""
                Prokeimenon and Verse in the Resurrection Tone for the week.
                Prokeimenon for the Saint in Tone VII: The saints shall boast in glory,
                * and they shall rejoice upon their beds.
            """
            ,'readings': """
                EPISTLE TO THE HEBREWS (DAY) (6:13 – 20)
                Brethren: when God made promise to Abraham, because he could swear by
                no greater, he sware by himself, Saying, Surely blessing I will bless thee, and
                multiplying I will multiply thee. And so, after he had patiently endured, he
                obtained the promise. For men verily swear by the greater: and an oath for
                confirmation is to them an end of all strife. Wherein God, willing more
                abundantly to shew unto the heirs of promise the immutability of his counsel,
                confirmed it by an oath: That by two immutable things, in which it was
                impossible for God to lie, we might have a strong consolation, who have fled for
                refuge to lay hold upon the hope set before us: Which hope we have as an
                anchor of the soul, both sure and steadfast, and which entereth into that within
                the veil; Whither the forerunner is for us entered, even Jesus, made an high priest
                for ever after the order of Melchisedec.
                EPISTLE TO THE EPHESIANS (SAINT) (5:9 – 19)
                Brethren: the fruit of the Spirit is in all goodness and righteousness and
                truth; Proving what is acceptable unto the Lord. And have no fellowship with
                the unfruitful works of darkness, but rather reprove them. For it is a shame even
                to speak of those things which are done of them in secret. But all things that are
                reproved are made manifest by the light: for whatsoever doth make manifest is
                light. Wherefore he saith, Awake thou that sleepest, and arise from the dead, and
                Christ shall give thee light. See then that ye walk circumspectly, not as fools, but
                as wise, Redeeming the time, because the days are evil. Wherefore be ye not
                unwise, but understanding what the will of the Lord is. And be not drunk with
                wine, wherein is excess; but be filled with the Spirit; Speaking to yourselves in
                psalms and hymns and spiritual songs, singing and making melody in your heart
                to the Lord;
                Alleluia and Verse in the Resurrection Tone of the week:
                Alleluia from the Triodion, in Tone VII:
                Verse: They that are planted in the house of the Lord, in the courts of
                our God they shall blossom forth.
                GOSPEL ACCORDING TO ST. MARK (DAY) (9:17-31)
                At that time: one of the multitude said, Master, I have brought unto thee my
                son, which hath a dumb spirit; And wheresoever he taketh him, he teareth him:
                and he foameth, and gnasheth with his teeth, and pineth away: and I spake to thy
                disciples that they should cast him out; and they could not. He answereth him,
                and saith, O faithless generation, how long shall I be with you? how long shall I
                suffer you? bring him unto me. And they brought him unto him: and when he
                saw him, straightway the spirit tare him; and he fell on the ground, and wallowed
                foaming. And he asked his father, How long is it ago since this came unto him?
                And he said, Of a child. And oft times it hath cast him into the fire, and into the
                waters, to destroy him: but if thou canst do any thing, have compassion on us,
                and help us. Jesus said unto him, If thou canst believe, all things are possible to
                him that believeth. And straightway the father of the child cried out, and said
                with tears, Lord, I believe; help thou mine unbelief. When Jesus saw that the
                people came running together, he rebuked the foul spirit, saying unto him, Thou
                dumb and deaf spirit, I charge thee, come out of him, and enter no more into
                him. And the spirit cried, and rent him sore, and came out of him: and he was as
                one dead; insomuch that many said, He is dead. But Jesus took him by the hand,
                and lifted him up; and he arose. And when he was come into the house, his
                disciples asked him privately, Why could not we cast him out? And he said unto
                them, This kind can come forth by nothing, but by prayer and fasting. And they
                departed thence, and passed through Galilee; and he would not that any man
                should know it. For he taught his disciples, and said unto them, The Son of man
                is delivered into the hands of men, and they shall kill him; and after that he is
                killed, he shall rise the third day.
                GOSPEL ACCORDING TO ST. MATHEW (SAINT) (4:25 - 5:12)
                At that time: there followed Jesus great multitudes of people from Galilee,
                and from Decapolis, and from Jerusalem, and from Judaea, and from beyond
                Jordan. And seeing the multitudes, he went up into a mountain: and when he was
                set, his disciples came unto him: And he opened his mouth, and taught them,
                saying, Blessed are the poor in spirit: for theirs is the kingdom of heaven. Blessed
                are they that mourn: for they shall be comforted. Blessed are the meek: for they
                shall inherit the earth. Blessed are they which do hunger and thirst after
                righteousness: for they shall be filled. Blessed are the merciful: for they shall
                obtain mercy. Blessed are the pure in heart: for they shall see God. Blessed are
                the peacemakers: for they shall be called the children of God. Blessed are they
                which are persecuted for righteousness’ sake: for theirs is the kingdom of heaven.
                Blessed are ye, when men shall revile you, and persecute you, and shall say all
                manner of evil against you falsely, for my sake. Rejoice, and be exceeding glad:
                for great is your reward in heaven:
            """
        } #Liturgy
    } #Service
    ,'-14': { #5th Sunday | St Mary of Egypt
        'vespers': {
            'stichera_tone': 'in Tone VIII;'
            ,'stichera': [
                """
                    The pollution of past defilements * prevented thee from gazing upon the
                    precious Cross * but thy spiritual awareness * and the actions of thy divinely-wise
                    conscience * turned thee to a better way of life. * And, having cast thine eyes
                    upon the icon of the blessed Maiden of God, * and repenting of all thy previous
                    transgressions, * O all-praised one, * with boldness thou didst venerate the
                    precious Cross.
                """
                ,"""
                    The pollution of past defilements * prevented thee from gazing upon the
                    precious Cross * but thy spiritual awareness * and the actions of thy divinely-wise
                    conscience * turned thee to a better way of life. * And, having cast thine eyes
                    upon the icon of the blessed Maiden of God, * and repenting of all thy previous
                    transgressions, * O all-praised one, * with boldness thou didst venerate the
                    precious Cross.
                """
                ,"""
                    Having worshipped at the holy places with great joy, * thou didst receive
                    that which was most beneficial for salvation * on the journey of the virtues, *
                    and with haste thou didst undertake * the journey chosen by thee. * Crossing the
                    stream of the Jordan, * with eagerness going to live in the dwelling-place of the
                    Baptist; * and taming the brutish passions by thy way of life, * thou didst boldly
                    bring into subjection, * O ever-memorable Mother, * the rebelliousness of the
                    flesh.
                """
                ,"""
                    Having gone to dwell in the desert wilderness, * thou didst wipe the
                    passions from thy soul, * and inscribing thereupon * the likeness of the most
                    supreme image of God, * thou didst become a reflection of the virtues, *
                    receiving whatsoever thou didst ask, * such as traversing the waters with ease O
                    blessed one, * and being raised up from the earth by thy prayers unto God. *
                    And now, all-glorious Mary, * since thou hast great boldness before Christ *
                    entreat Him on behalf of our souls.
                """
            ]
            ,'doxastichon': """
                in Tone IV:
                The power of Thy Cross, O Christ, * hath wrought great wonders, * for the
                woman who was once a harlot, * through ascetic endeavors * followed the life of
                abstinence, * from whence having cast aside her weakness, * she bravely stood in
                opposition to the devil; * wherefore carrying the prize of victory, * she ever
                intercedeth on behalf of our souls.
            """
            ,'aposticha_theotokion': """
                Glory ..., From the Triodion, in Tone II:
                The sensual desires of thy soul and the passions of thy flesh * didst thou
                slay with the sword of abstinence; * thy sinful thoughts didst thou stifle by
                silence. * With the streams of thy tears thou didst wholly water the desert
                wilderness, * blossoming forth for us the fruits of repentance: * Wherefore, O
                venerable one, we celebrate thy memory.
                Now & ever ..., in Tone II:
                O new wonder greater than all the wonders of old! * For who hath ever
                known a mother to give birth without having known a man, * and to bear on her
                arm Him Who sustaineth all creation? * Yet it was the will of God to be born. *
                O most pure one, who carried Him as an infant in Thine embrace * and before
                Whom thou hast a mother’s boldness: * cease not to pray on behalf of those
                who honor thee, ** that He have compassion and save our souls.
            """
        } #Vespers
        ,'matins': {
            'troparion': """
                Troparion to Saint Mary, in Tone VIII:
                In thee, O mother, the image of God was preserved, * for taking up thy
                cross, thou didst follow after Christ; * by activity thou didst learn to disdain the
                flesh, as something transient, * but to care for thy soul as something immortal. **
                Wherefore, with the angels thy spirit doth rejoice, O venerable Mary.
                Resurrection Theotokion, in Tone VIII:
                O Good One, Who for our sake wast born of the Virgin * and, having
                endured crucifixion, cast down death by death, * and as God revealed the
                resurrection: * disdain not that which Thou hast fashioned with Thine own hand.
                * Show forth Thy love for mankind, O Merciful One; * Accept the supplications
                of the Theotokos who bore Thee, ** and save Thy despairing people, O our
                Savior!
            """
            ,'after50': """
                in Tone VIII:
                Glory ..., The gates of repentance, do Thou open unto me, O Giver of Life, *
                for early in the morning my spirit seeketh Thy holy temple, * bearing the temple
                of my body all defiled. * But as One who art compassionate * cleanse it by Thy
                loving-kindness and mercy.
                Now & ever ..., Guide me on the paths of salvation, O Theotokos: * for I
                have polluted my soul with shameful deeds * and wasted all my life in
                slothfulness. * but by thine intercessions * do thou deliver me from all impurity.
                In Tone VI:
                Have mercy upon me, O God, * according to Thy great mercy: * and
                according to the multitude of Thy compassion * blot out my transgressions.
                In Tone VIII: As I the wretched one ponder the multitude of evil deeds I
                have done, * I tremble for fear of the dread day of judgment. * But trusting in
                Thy compassionate mercy, * like David do I cry unto Thee: * “Have mercy upon
                me, O God, according to Thy great mercy”.
            """
            ,'canon': """
                ODE I
                The appointed Canons from the Oktoechos. Then:
                The fist Canon from the Triodion, in Tone VIII:
                Irmos: Having passed through the water as upon dry land ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                Thou hast abandoned me due to mine abundant lusts, having each day taken
                enjoyment in them like the rich man. Wherefore I pray unto Thee O Savior;
                deliver me from the fire as Thou didst once deliver Lazarus.
                Refrain: Have mercy on me, O God, have mercy on me.
                I am clothed in sensual pleasures, O Savior, like the rich man who once
                vested himself in fine linen, gold, and golden clothing, but send me not into the
                fire, as Thou didst him.
                Refrain: Have mercy on me, O God, have mercy on me.
                Having taken pleasure in the riches and sweet things of this corruptible life,
                the rich man of old was condemned to torments, whereas the needy Lazarus
                obtained consolation.
                Refrain: Most holy Theotokos save us.
                The hosts of angels and mortals ceaselessly praise thee O Mother unwedded
                for thou didst carry their creator as a babe in thine arms.
                Of the Saint, in Tone VI:
                Irmos: He Who in ancient times hid the pursuing tyrant ...,
                Refrain: Venerable Mother Mary, Pray to God for us.
                With love I celebrate thy light-giving and holy memory, do thou send down
                to me the unapproachable light of Christ O venerable one, before Whom thou
                dost now stand, and deliver me from the manifold temptations of life.
                Refrain: Venerable Mother Mary, Pray to God for us.
                He Who fled unto the Egyptians in the flesh, the un-circumscribable and
                eternal One, hath revealed thee to be a most radiant beacon issuing forth from
                whence He once dwelt; Egypt.
                Glory ..., Not knowing the divine commandments, thou didst sully the
                divine image of God within thee, but, O all-praised one, through divine
                providence, thou didst cleanse it once again, rendering thyself godlike by thy
                godly actions, O venerable one.
                Now & Ever ..., O my God, great is Thy loving-kindness, and ineffable Thy
                condescension! For, by the intercessions of Thy Mother, Thou didst render the
                former harlot as pure and spotless, as the angels.
                Katavasia: I shall open my mouth, * and be filled with the Spirit, * and
                utter discourse to the Queen and Mother; * and be seen radiantly keeping
                festival, * joyfully praising her wonders.
                ODE III
                The appointed Canons from the Oktoechos. Then:
                The fist Canon from the Triodion, in Tone VIII:
                Irmos: Thou art the strengthening of all who come to Thee ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                O Christ, as Thou didst save Lazarus from the flames, do Thou also deliver
                me, Thine unworthy servant, from the fire of Gehenna.
                Refrain: Have mercy on me, O God, have mercy on me.
                O Lord, in passions and lusts I am as wealthy as the rich man, yet in my lack
                of virtues I am as poor as Lazarus. But do Thou save me.
                Refrain: Have mercy on me, O God, have mercy on me.
                The rich man clothed himself in scarlet and fine linen - lusts and sins, for
                which sake he was cast into the flames.
                Refrain: Most holy Theotokos save us.
                Grant unto us help, by thine intercessions O all-pure one, who canst deliver
                us from every evil circumstance.
                Of the Saint, in Tone VI:
                Irmos: When the creation beheld Thee ...,
                Refrain: Venerable Mother Mary, Pray to God for us.
                Thou didst draw near to the gates of destruction by thine inexcusable
                actions; but He Who of old, by the power of His Godhead, smashed to pieces
                the gates of Hades, opened unto thee the gates of repentance, O all-honored
                one; for He Himself is the Gate of life.
                Refrain: Venerable Mother Mary, Pray to God for us.
                She who was once a weapon of sin, O Longsuffering One, hath now been
                revealed to be a weapon of Thy Cross, O Compassionate One, for by venerating
                it, she conquered all the weapons and cunning of the devils.
                Glory ..., He who shed His own blood as a ransom for the sake of all, in the
                waters of thy tears cleansed thee who wast grievously sickened with the leprosy
                of thy wicked deeds, for He is the cause of all that is.
                Now & Ever ..., That which hath come to pass within Thee, O Virgin,
                transcends description: For the Word of the Father came to dwell within Thee,
                granting by His word alone, the remission of sins unto all those who transgress.
                Katavasia: O Theotokos, thou living and plentiful fount, * establish in
                spiritual fellowship those who sing hymns to thee, * and in thy divine
                glory * grant them crowns of glory.
                Kontakion of the Saint, in Tone III:
                Thou wast once defiled with all manner of impurities, * but today through
                repentance thou hast become the Bride of Christ. * desiring to follow the life of
                the angels, * thou didst cast down demons by the weapon of the Cross: * For
                which sake O all-glorious Mary, * thou art a bride of the Kingdom.
                Ikos: As the lamb and daughter of Christ we now praise thee in our hymns,
                O ever-memorable Mary. Sprung from the race of the Egyptians, thou didst flee
                from all their delusions and alone offered thyself to the Church as an example of
                perfection, in abstinence and prayer struggling above that which is the measure
                of man’s nature, wherefore the only Pantocrator hath exalted thee, thy life and
                actions, O most-glorious Mary.
                Sessional Hymns in Tone VIII:
                Spec. Mel.: “Of the Wisdom ...”;
                All the rebelliousness of the flesh didst thou subdue by thine ascetic labors,
                * showing the manly wisdom of thy soul. * Desiring to behold the Cross of the
                Lord, O all-honored one, * thou didst crucify thyself to the world, * eagerly
                seeking to emulate the angels in their way of life. * Wherefore with faith we
                honor thy memory, O all-blessed one, * and beseech thee to pray on our behalf,
                * that we may be granted the full remission of our sins ** by thine intercessions.
                Glory ..., Now & Ever ..., Let us hymn the heavenly gate and ark, * the allholy Mountain and the Cloud of light, * the heavenly Ladder and the spiritual
                Paradise, * the Deliverance of Eve and the great Treasure of the whole world. *
                For through her was wrought the salvation of the world * and the remission of
                man’s ancient sins. * Wherefore we cry aloud unto her: * “Pray to thy Son and
                God, * that remission of sins be granted to those ** who devoutly worship thine
                all-holy offspring”.
                ODE IV
                The appointed Canons from the Oktoechos. Then:
                The fist Canon from the Triodion, in Tone VIII:
                Irmos: I have heard, O Lord, the mystery of Thy plan ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                The rich man took delight in sumptuous food and raiment, while Lazarus
                longed to be fed with the crumbs that fell from his table.
                Refrain: Have mercy on me, O God, have mercy on me.
                With their tongues the dogs licked the sores of Lazarus the beggar, showing
                themselves to be more compassionate to the poor than the rich man.
                Refrain: Have mercy on me, O God, have mercy on me.
                Before the gates of the rich man, O Savior, Lazarus once lay wretched and
                suffering from his wounds, but now he is glorified.
                Refrain: Most holy Theotokos save us.
                Beseech Him whom thou didst bear, O most pure one, that those who
                hymn thee may be saved from the machinations of the deceiver, for thou alone
                art our sure protector.
                Of the Saint, in Tone VI:
                Irmos: Foreseeing Thy divine self-emptying upon the Cross ...,
                Refrain: Venerable Mother Mary, Pray to God for us.
                O Creator of the mortal nature of man, since Thou art a fount of mercy and
                a wealth of compassion, O Lover of mankind, Thou didst have compassion
                upon her that fled unto Thee for refuge, snatching her away from the destroying
                beast.
                Refrain: Venerable Mother Mary, Pray to God for us.
                Hastening to see the Cross, thou wast illumined by its effulgence O Mary,
                and having communed with it, by the divine manna of Him who was crucified
                thereon, thou didst become crucified to the world O right wondrous one.
                Glory ..., Previously guilty of leading many astray by wicked lust, thou dost
                now shine forth like the sun, manifesting thyself as a guide to all transgressors, O
                venerable one.
                Now & Ever ..., Thou hast surpassed the mind of the noetic heavenly
                powers of the King of all; for transcending the laws of nature, O pure one, Thou
                didst give birth to the Lawgiver and Fashioner of all things.
                Katavasia: He who sitteth in glory upon the throne of the Godhead, *
                Jesus the true God, * is come in a swift cloud * and with His sinless hands
                he hath saved those who cry: * Glory to Thy power, O Christ.
                ODE V
                The appointed Canons from the Oktoechos. Then:
                The fist Canon from the Triodion, in Tone VIII:
                Irmos: O Light that never sets ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                When the rich man saw Lazarus resting in the bosom Abraham, rejoicing in
                light and glory, he cried aloud: “O Father Abraham, have mercy on me, for I am
                condemned to the fire and my tongue doth burn in bitter torment.”
                Refrain: Have mercy on me, O God, have mercy on me.
                “During thy life,” said Abraham to the rich man, “thou didst rejoice living
                sumptuously; wherefore thou art now eternally tormented in the fire, while
                Lazarus the beggar rejoiceth in unending gladness.”
                Refrain: Have mercy on me, O God, have mercy on me.
                The life of the rich man was one of delusion in pleasure, and I, like the rich
                man, also live a sumptuous life, but I beseech of Thee compassion, O Lover of
                mankind, that I may be delivered from the fire, as Thou didst once save Lazarus.
                Refrain: Most holy Theotokos save us.
                Possessing maternal boldness before thy Son, O all-pure one, we beseech
                thee who art from our lineage, turn not away from us, for thee alone do we
                Christians bring before the Lord, as a God-pleasing intercessor on our behalf.
                Of the Saint, in Tone VI:
                Irmos: Thy Theophany, O Christ, the Unwaning Light ...,
                Refrain: Venerable Mother Mary, Pray to God for us.
                Moses once shone in glory on Mount Sinai, for having mystically beheld the
                most glorious hind-parts of God, he himself became a reflection of the strange
                mystery; and now, fervently falling down before the image of the most-pure one,
                the vessel which contained the Manna from heaven, Mary undertakes the angelic
                life.
                Refrain: Venerable Mother Mary, Pray to God for us.
                Having longed, like the psalmist, to see the majesty of the temple, the noetic
                tabernacle of Thy glory, she who defiled the temple cried; “by the noetic prayers
                O Christ, and of her who became Thy temple, without knowing a man, make me
                a temple of the all-creating Spirit”.
                Glory ..., With the baited hook of the flesh, she caught the eye of many, and
                by short-lived sensual pleasure she made them food for the devil, but in truth
                having been caught by the divine grace of the precious Cross, she became the
                most sweet food of Christ.
                Now & Ever ..., Having learnt of the mystery concerning thee, the choir of
                the prophets hath, with mystical divinely spoken words O most-pure one,
                prophesied concerning thee in many ways. And now Mary, having fallen down
                before the most pure image of thee, the Vessel that received the divine Manna,
                she hath become a sure intercessor for us sinners before God.
                Katavasia: All creation stands in awe of thy divine glory; * for thou, O
                Virgin who hast not known wedlock, * didst contain within thy womb the
                God of all, * and gave birth to the timeless Son, * bestowing peace, upon
                all who hymn thee.
                ODE VI
                The appointed Canons from the Oktoechos. Then:
                The fist Canon from the Triodion, in Tone VIII:
                Irmos: Cleanse me, O Savior ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                The rich man condemned himself to the flames of fire by his life of
                pleasure; but Lazarus the poor man chose poverty in this present life, and so was
                deemed worthy of unending joy.
                Refrain: Have mercy on me, O God, have mercy on me.
                Lazarus was deemed worthy to dwell in the bosom of Abraham, enjoying
                eternal life, O Christ; but the rich man was condemned to the fire, to be
                tormented in both soul and body.
                Refrain: Have mercy on me, O God, have mercy on me.
                The rich man was condemned to the fire because of Lazarus, do Thou
                condemn me not, wretched as I am, but I pray Thee O Lover of mankind, grant
                me, like Lazarus, O Lord, Thy light.
                Refrain: Most holy Theotokos save us.
                May we be delivered from grievous sins, by thy prayers O pure Mother of
                God, and may we be granted the divine enlightenment of the Son of God, who
                ineffably took flesh from thee.
                Of the Saint, in Tone VI:
                Irmos: Jonah was caught but not held ...,
                Refrain: Venerable Mother Mary, Pray to God for us.
                The armies of the angels rejoice, O holy Mary, seeing in thee a life equal to
                their own, and crying out they give glory to the Lord.
                Refrain: Venerable Mother Mary, Pray to God for us.
                The host of dark spirits tremble at the strength of thy patient endurance,
                marveling at how a woman naked and alone, hath been able to wondrously
                overcome them.
                Glory ..., Thou hast shone forth like the sun O all-praised Mary, illumining
                the desert with thy wonders, do thou also make me radiant with light.
                Now & Ever ..., The angels, illumined by the glory of thine Offspring, O
                Virgin, proclaim to all; peace on earth and good will toward mankind.
                Katavasia: Celebrating the divine and solemn feast * of the Mother of God
                * O ye divinely wise, * let us come, clapping our hands, * and glorify God
                who was born of her.
                Kontakion and Ikos of the Resurrection in the Tone of the week
                SYNAXARION READING
                Verse: The spirit departed, the flesh was left untended long ago;
                Verse: Hide, O Earth, the mortal bones of Mary.
                On this day, the fifth Sunday of the Fast, we have been enjoined to make
                commemoration of our righteous Mother Mary of Egypt.
                She, while yet twelve years of age, came to Alexandria unbeknownst to her
                parents, and there lived a profligate life for seventeen years. Afterwards, being
                moved by curiosity, she departed with many other worshippers for Jerusalem, in
                order to be present for the Exaltation of the Precious Cross. There, she gave
                herself over to every form of licentiousness and impropriety, and dragged many
                others down to the depths of destruction. On the day in which the Cross was
                exalted, she, when she desired to enter the church, felt some invisible power
                preventing her from passing through the entrance, though she tried a third and
                even a fourth time, and though the multitude that was with her passed through
                the same entrance unhindered. Because her heart was wounded by this, she
                decided to change her life, and to propitiate God through repentance. And thus
                when she returned to the church, she entered easily therein. After venerating the
                Precious Cross, that very day she withdrew from Jerusalem, passed over the
                Jordan, entered the inner regions of the desert, and there she lived the hardest
                life, a super-human life, for forty-seven years, praying alone to God alone.
                Concerning the end of her life: After meeting a certain monastic, Zosimas by
                name, and fully recounting to him her life from the beginning, she begged him to
                bring to her the spotless mysteries for Communion. And he did this very thing
                the following year, on Holy Thursday. The year after that Zosimas, coming once
                again, found her dead, stretched out upon the earth; and beside her was written
                the following: "Abba Zosimas, bury here the body of wretched Mary. I departed
                in death the very day in which I communed of the spotless mysteries. Pray for
                me." Her death took place in the year 378. The memory of this righteous woman
                is celebrated on the first of every April; but the same is also appointed for today,
                since the end of the sacred forty-day fast now draws near, in order to rouse the
                slothful and the sinners unto repentance, since they have an example in her, the
                Saint who is being celebrated.
                Through her intercessions, O God,
                have mercy on us and save us.
                Amen.
                ODE VII
                The appointed Canons from the Oktoechos. Then:
                The fist Canon from the Triodion, in Tone VIII:
                Irmos: The Hebrew youths did boldly tread ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                Like Job of old, who sat on a dung heap full of decaying filth and worms,
                Lazarus lay before the gates of the rich man, crying: “O God of our fathers,
                blessed art Thou.”
                Refrain: Have mercy on me, O God, have mercy on me.
                An outcast at the gate of the heartless rich man, Lazarus of old, longed for
                the crumbs that fell from his table, yet no man gave to him; and in place of this
                he was granted to dwell in the bosom of Abraham.
                Refrain: Have mercy on me, O God, have mercy on me.
                O my Christ, I pray Thee, deliver me from the lot of the heartless rich man,
                and number me with Lazarus the poor man, that I may be deemed worthy to cry
                unto Thee with thanksgiving “O God of our fathers, blessed art Thou”.
                Refrain: Most holy Theotokos save us.
                Thou didst appear incarnate from the virginal womb for our salvation.
                Wherefore we acknowledge Thy mother as the Theotokos, and with thanksgiving
                cry aloud: “O God of our fathers, blessed art Thou”.
                Of the Saint, in Tone VI:
                Irmos: O ineffable wonder! He Who delivered the holy Children ...,
                Refrain: Venerable Mother Mary, Pray to God for us.
                Wise Zosimas, greatest among the fathers, wandered in the desert wilderness
                and was counted worthy to see the venerable mother, and cried aloud; “O God
                of our fathers, Blessed art Thou”.
                Refrain: Venerable Mother Mary, Pray to God for us.
                “For what O father”, said the venerable one to the staretz “didst thou come
                to see a woman who is a stranger to every manner of virtuous action” and she
                cried aloud; “O God of our fathers, Blessed art Thou”.
                Glory ..., Thou didst put to death O blessed one, the rebelliousness of thy
                passions, and now having striven to the safe haven of passionlessness thou dost
                cry aloud; “O God of our fathers, Blessed art Thou”.
                Now & Ever ..., In ways transcending speech, O most-pure one, Thou didst
                conceive while yet remaining a virgin, and didst bring forth into the world the
                salvation, Christ our God. Wherefore we and all the faithful magnify Thee in
                songs.
                Katavasia: Refusing to worship created things * in place of the Creator, *
                the divinely wise youths bravely trampled down the threatening fire * and
                rejoicing they sang aloud: * O supremely hymned Lord and God of our
                Fathers, Blessed art Thou.
                ODE VIII
                The appointed Canons from the Oktoechos. Then:
                The fist Canon from the Triodion, in Tone VIII:
                Irmos: In his wrath the Chaldean Tyrant made the furnace blaze ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                In clothes of scarlet raiment, fine linen and purple, the rich man of old
                splendidly clothed himself in wretchedness, while the poor man Lazarus lay a
                pitiable outcast at his gate, longing to eat the crumbs that fell from the rich man’s
                table; and no man gave to him. But now he reigneth with Christ in glory.
                Refrain: Have mercy on me, O God, have mercy on me.
                Lazarus lay at the gates of the rich man, his body putrid with sores: He
                longed to eat, and no man gave him food; but the dogs, moved by compassion,
                licked his sores and wounds. Wherefore he hath been deemed worthy of joy in
                Paradise.
                Refrain: Have mercy on me, O God, have mercy on me.
                I have grown rich in sensual pleasures, like the rich man of old, clothing
                himself each day in scarlet; and I have condemned myself by taking pleasure and
                being deceived by the sweet things of this life, O Compassionate One.
                Wherefore I pray to Thee, O Christ, deliver me from the eternal fire throughout
                all ages.
                Refrain: Most holy Trinity our God glory be to Thee.
                The threefold light of the Godhead shineth with a single radiance, from one
                Hypostatic essence, The Father without beginning, the Son of the same essence
                as the father, and the co-enthroned consubstantial Spirit, O ye children bless, ye
                priest praise, and ye peoples supremely exalt throughout all ages.
                Of the Saint, in Tone VI:
                Irmos: Be ye astonished and afraid, O heaven ...,
                Refrain: Venerable Mother Mary, Pray to God for us.
                He Who searcheth the depths of the heart, and who, before we came into
                being, foreseeth all things concerning us, hath freed from a life of bondage the
                woman who fled to Thee, O Savior; in need of Thy love for mankind she cried
                out to Thee with never-silent voice: “O ye priests bless Him, and ye people
                supremely exalt Him throughout all ages.”
                Refrain: Venerable Mother Mary, Pray to God for us.
                O Honorable is the change of life, that hath brought thee to a better way! O
                divine the love that hath taught thee to despise the sensual pleasures of the flesh!
                O all-praised Mary, fervent and divine in the faith, which we faithfully praise and
                supremely exalt throughout the ages.
                Refrain: Let us bless Father, Son, Holy Spirit, the Lord!
                Thou didst receive a recompense for thy sufferings, and a reward for thy
                labors, O honored Mary, by which thou didst slay the murderous enemy: and
                now with the angels thou dost cry aloud with never-ceasing hymns supremely
                exalting Christ throughout the ages.
                Now & Ever ..., For the sake of His goodness the Lord of all the ages hath
                completely renewed me within thy womb, O pure one, without commingling that
                which is unique to each nature. Wherefore, as the cause of our salvation, with
                hymns we praise thee throughout all ages.
                Refrain: We praise, bless and worship the Lord, chanting and supremely
                exalting Him throughout all ages.
                Katavasia: The Offspring of the Theotokos * saved the holy children in the
                furnace. * He who was then prefigured hath now been born on earth, *
                and He gathereth all creation to hymn thee: * all ye works praise ye the
                Lord * and supremely exalt Him throughout all ages.
                And then we chant the Hymn of the Most Holy Theotokos (the Magnificat)
                ODE IX
                The appointed Canons from the Oktoechos. Then:
                The fist Canon from the Triodion, in Tone VIII:
                Irmos: With never ceasing praises we magnify thee ...,
                Refrain: Have mercy on me, O God, have mercy on me.
                I pray Thee, O Christ, make me like Lazarus the beggar, banishing my desire
                for sensual pleasure, since Thou art God in essence: and make me as wealthy as
                the rich man, only, in the virtues, that with faith I may magnify Thee in hymns.
                Refrain: Have mercy on me, O God, have mercy on me.
                Rich and unmerciful, my mind hath despised faith in Thy commandments,
                O Lover of mankind, and been cast out before the gates. But since Thou art a
                fellow sufferer, and lovingly compassionate, raise it up as once Thou didst raise
                up Thy friend Lazarus, who was four days dead.
                Refrain: Have mercy on me, O God, have mercy on me.
                All have learnt the meaning of this parable of the Lord, let us, the faithful
                despise the lack of compassion of the rich man, that we may escape torments,
                and eternally rejoice in the bosom of Abraham.
                Refrain: Most holy Theotokos save us.
                The invisible God hast thou carried in thine arms, He who is praised in the
                heavens and by all of creation, by thee we have been granted salvation at all
                times, wherefore with faith we magnify thee.
                Of the Saint, in Tone VI:
                Irmos: Weep not for Me, O Mother ...,
                Refrain: Venerable Mother Mary, Pray to God for us.
                Thou didst more easily endure thy labors in the wilderness; strengthened by
                the almighty strength of Christ, quenching the impure thoughts that came to
                thee, by the streams of thy godly tears, O mother, the summit of ascetics and
                glory of the venerable saints.
                Refrain: Venerable Mother Mary, Pray to God for us.
                With rays of exceeding brightness, the only birth-giver of Christ the light,
                the pure virgin, shone upon thee, making thee frightening to thine enemies O
                honored one; and revealing thee to us all O Mary, as the beauty of ascetics, and
                the foundation of venerable saints.
                Glory ..., Having wisely abandoned all the things of this world, thou didst
                become a sacred dwelling of the Spirit: Beseech Christ the Redeemer, that we
                who faithfully celebrate thy memory may be freed from the grief of worldly
                passions.
                Now & Ever ..., In a manner transcending nature, O Virgin, thou hast been
                freed from the laws of nature, and brought forth on earth a newborn Child, Who
                is the Giver of the Law and the Ancient of Days. Wherefore, O noetic heaven of
                the Creator of all, with faith and love we call thee blessed.
                Katavasia: Let every mortal born on earth, * radiant with light, in spirit
                leap for joy; * and let the host of the angelic powers * celebrate and honor
                the holy feast of the Mother of God, * and let them cry aloud: * Rejoice! O
                Theotokos, thou pure Ever-Virgin.
            """
            ,'exapostilarion': """
                Glory ... Exapostilarion from the Triodion, in Tone III:
                Thee do we have as an image of repentance, * O all-venerable Mary, * pray
                to Christ that in the season of the Fast * we may also be granted repentance, **
                that with faith and love we may praise thee with hymns.
                Now & ever ... Theotokion from the Triodion, in Tone III:
                O sweetness of the angels, * joy of the afflicted, * intercessor on behalf of
                Christians, * Virgin Mother of the Lord, ** help me and deliver me from eternal
                torment.
            """
            ,'praises':"""

            """
            ,'aposticha': """
                in Tone I:
                9th Verse: Arise, O Lord my God, let Thy hands be lifted high; * forget
                not Thy paupers to the end.
                The Kingdom of God is not food and drink, * but righteousness and
                abstinence with holiness: * And so the rich shall not enter into it, * but those
                who invest their treasures into the needful hands of the poor. * This is what
                David the Prophet hath taught us, saying: * “The righteous man showeth mercy
                all the day long; * his delight is in the Lord, and walking in the light he shall not
                stumble”. * All this was written for our admonition, that we fast and undertake
                the doing of good deeds; * that in place of earthly things ** the Lord may grant
                us heavenly things.
            """
            ,'aposticha_theotokion': """
                Theotokion, in Tone II:
                Thou art most blessed, O Virgin Theotokos, * for through Him who took
                flesh from thee, Hades hath been captured, * Adam recalled, the curse slain, Eve
                set free, * death put to death, and we have been given life. * Therefore in praise
                we cry: ** Blessed art Thou, O Christ our God, who hast been thus well-pleased,
                glory be to Thee.
            """
        } #Matins
        ,'liturgy': {
            'troparion':"""
                Troparion of the Saint, in Tone VIII:
                In thee, O mother, the image of God was preserved, * for taking up thy
                cross, thou didst follow after Christ; * by activity thou didst learn to disdain the
                flesh, as something transient, * but to care for thy soul as something immortal. **
                Wherefore, with the angels thy spirit doth rejoice, O venerable Mary.
            """
            ,'kontakion': """
                Kontakion of the Saint, in Tone III:
                Glory ..., Thou wast once defiled with all manner of impurities, * but today
                through repentance thou hast become the Bride of Christ. * desiring to follow
                the life of the angels, * thou didst cast down demons by the weapon of the
                Cross: * For which sake O all-glorious Mary, * thou art a bride of the Kingdom.
                Now & Ever ..., in Tone VI:
                O protection of Christians that cannot be put to shame, * O mediation unto
                the Creator unfailing, * disdain not the suppliant voices of sinners, * but be thou
                quick, O good one, to help us who in faith cry unto thee; * hasten to intercession
                and speed thou to make supplication, ** thou who dost ever protect, O
                Theotokos, them that honor thee.
            """
            ,'readings': """
                EPISTLE TO THE HEBREWS (9:11 – 14)
                Brethren: Christ being come an high priest of good things to come, by a
                greater and more perfect tabernacle, not made with hands, that is to say, not of
                this building; Neither by the blood of goats and calves, but by his own blood he
                entered in once into the holy place, having obtained eternal redemption for us.
                For if the blood of bulls and of goats, and the ashes of an heifer sprinkling the
                unclean, sanctifieth to the purifying of the flesh: How much more shall the blood
                of Christ, who through the eternal Spirit offered himself without spot to God,
                purge your conscience from dead works to serve the living God?
                EPISTLE TO THE GALAIONS (3:23 - 29)
                Brethren: before faith came, we were kept under the law, shut up unto the
                faith which should afterwards be revealed. Wherefore the law was our
                schoolmaster to bring us unto Christ, that we might be justified by faith. But
                after that faith is come, we are no longer under a schoolmaster. For ye are all the
                children of God by faith in Christ Jesus. For as many of you as have been
                baptized into Christ have put on Christ. There is neither Jew nor Greek, there is
                neither bond nor free, there is neither male nor female: for ye are all one in
                Christ Jesus. And if ye be Christ’s, then are ye Abraham’s seed, and heirs
                according to the promise.
                Alleluia and Verse in the Resurrection Tone of the week:
                Alleluia, in Tone I: With patience I waited patiently for the Lord, and
                He was attentive unto me, and He hearkened unto my supplication.
                GOSPEL ACCORDING TO ST. MARK (10:32 – 45)
                At that time: His disciples were in the way going up to Jerusalem; and Jesus
                went before them: and they were amazed; and as they followed, they were afraid.
                And he took again the twelve, and began to tell them what things should happen
                unto him, Saying, Behold, we go up to Jerusalem; and the Son of man shall be
                delivered unto the chief priests, and unto the scribes; and they shall condemn
                him to death, and shall deliver him to the Gentiles: And they shall mock him,
                and shall scourge him, and shall spit upon him, and shall kill him: and the third
                day he shall rise again. And James and John, the sons of Zebedee, come unto
                him, saying, Master, we would that thou shouldest do for us whatsoever we shall
                desire. And he said unto them, What would ye that I should do for you? They
                said unto him, Grant unto us that we may sit, one on thy right hand, and the
                other on thy left hand, in thy glory. But Jesus said unto them, Ye know not what
                ye ask: can ye drink of the cup that I drink of? and be baptized with the baptism
                that I am baptized with? And they said unto him, We can. And Jesus said unto
                them, Ye shall indeed drink of the cup that I drink of; and with the baptism that
                I am baptized withal shall ye be baptized: But to sit on my right hand and on my
                left hand is not mine to give; but it shall be given to them for whom it is
                prepared. And when the ten heard it, they began to be much displeased with
                James and John. But Jesus called them to him, and saith unto them, Ye know
                that they which are accounted to rule over the Gentiles exercise lordship over
                them; and their great ones exercise authority upon them. But so shall it not be
                among you: but whosoever will be great among you, shall be your minister: And
                whosoever of you will be the chiefest, shall be servant of all. For even the Son of
                man came not to be ministered unto, but to minister, and to give his life a
                ransom for many.
                GOSPEL ACCORDING TO ST. LUKE (7:36 – 50)
                At that time: one of the Pharisees desired him that he would eat with him.
                And he went into the Pharisee’s house, and sat down to meat. And, behold, a
                woman in the city, which was a sinner, when she knew that Jesus sat at meat in
                the Pharisee’s house, brought an alabaster box of ointment, And stood at his feet
                behind him weeping, and began to wash his feet with tears, and did wipe them
                with the hairs of her head, and kissed his feet, and anointed them with the
                ointment. Now when the Pharisee which had bidden him saw it, he spake within
                himself, saying, This man, if he were a prophet, would have known who and
                what manner of woman this is that toucheth him: for she is a sinner. And Jesus
                answering said unto him, Simon, I have somewhat to say unto thee. And he
                saith, Master, say on. There was a certain creditor which had two debtors: the
                one owed five hundred pence, and the other fifty. And when they had nothing to
                pay, he frankly forgave them both. Tell me therefore, which of them will love
                him most? Simon answered and said, I suppose that he, to whom he forgave
                most. And he said unto him, Thou hast rightly judged. And he turned to the
                woman, and said unto Simon, Seest thou this woman? I entered into thine house,
                thou gavest me no water for my feet: but she hath washed my feet with tears, and
                wiped them with the hairs of her head. Thou gavest me no kiss: but this woman
                since the time I came in hath not ceased to kiss my feet. My head with oil thou
                didst not anoint: but this woman hath anointed my feet with ointment.
                Wherefore I say unto thee, Her sins, which are many, are forgiven; for she loved
                much: but to whom little is forgiven, the same loveth little. And he said unto her,
                Thy sins are forgiven. And they that sat at meat with him began to say within
                themselves, Who is this that forgiveth sins also? And he said to the woman, Thy
                faith hath saved thee; go in peace.
            """
        } #Liturgy
    } #Service
    ,'-8': { #Lazarus Saturday
        'vespers': {
            'stichera_tone': ''
            ,'stichera': [
                """
                    Having completed the spiritually profitable forty days, * we entreat Thee O
                    Lover of mankind: * Grant us also to behold the Holy Week of Thy Passion, *
                    that in it we may glorify Thy mighty acts * and Thine ineffable dispensation for
                    our sakes, * so that with one mind we may chant: ** “O Lord, glory be to Thee”.
                """
                ,"""
                    Having completed the spiritually profitable forty days, * we entreat Thee O
                    Lover of mankind: * Grant us also to behold the Holy Week of Thy Passion, *
                    that in it we may glorify Thy mighty acts * and Thine ineffable dispensation for
                    our sakes, * so that with one mind we may chant: ** “O Lord, glory be to Thee”.
                """
                ,"""
                    O ye martyrs of the Lord, * pray ye on our behalf to God, * beseech Him to
                    grant abundant mercy to our souls ** and the forgiveness of our many
                    transgressions.
                """
                ,"""
                    O Lord, wishing to see the tomb of Lazarus, * Thou Who willed to be placed
                    in a tomb, didst ask: * “Where have ye laid him?” * And, learning that which was
                    not unknown to Thee, * Thou didst cry aloud to him whom Thou didst love: *
                    “Lazarus, come forth.” * And he who was without breath * obeyed the One who
                    gave him breath, ** even Thee, the Savior of our souls
                """
                ,"""
                    O Lord, wishing to see the tomb of Lazarus, * Thou Who willed to be placed
                    in a tomb, didst ask: * “Where have ye laid him?” * And, learning that which was
                    not unknown to Thee, * Thou didst cry aloud to him whom Thou didst love: *
                    “Lazarus, come forth.” * And he who was without breath * obeyed the One who
                    gave him breath, ** even Thee, the Savior of our souls
                """
                ,"""
                    O Lord, after four days Thou didst come to the tomb of Lazarus, * and
                    shedding tears over the tomb * Thou didst raise up him who was four days dead,
                    * O Wheat of life, * wherefore death was bound by Thy voice, * and the graveclothes were loosed by Thy hands. * Then the multitude of Thy disciples were
                    filled with joy, * and with one voice cried aloud: ** “Blessed art Thou, O Savior,
                    have mercy on us”.
                """
                ,"""
                    O Lord, after four days Thou didst come to the tomb of Lazarus, * and
                    shedding tears over the tomb * Thou didst raise up him who was four days dead,
                    * O Wheat of life, * wherefore death was bound by Thy voice, * and the graveclothes were loosed by Thy hands. * Then the multitude of Thy disciples were
                    filled with joy, * and with one voice cried aloud: ** “Blessed art Thou, O Savior,
                    have mercy on us”.
                """
                ,"""
                    O Lord, Thy voice hath destroyed the dominion of Hades, * and the Word of
                    Thy power hath raised from the tomb, * him that had been four days dead; *
                    whereby Lazarus became the first-fruit * of the saving transformation of the
                    world. * All things are possible to Thee, O Lord and King of all. ** Bestow upon
                    Thy servants forgiveness and great mercy
                """
                ,"""
                    O Lord, wishing to grant Thy disciples * an assurance of Thy Resurrection
                    from the dead, * Thou didst come to the tomb of Lazarus * and having called
                    him by name, Hades was despoiled, * and released the one that had been four
                    days dead, * as he called out to Thee: ** “O blessed Lord, glory be to Thee”.
                """
                ,"""
                    O Lord, taking Thy disciples, * Thou didst come to Bethany to awaken
                    Lazarus: * and Thou didst weep for him in accordance with the law of human
                    nature, * but as God Thou didst raise up the four-day corpse, * and he cried out
                    to Thee, O Savior: ** “O blessed Lord, glory be to Thee”.
                """
            ]
            ,'doxastichon': """
                    Glory ..., from the Triodion, in Tone VIII:
                    Standing before the tomb of Lazarus, O our Savior, * and having called out
                    to the dead man, * Thou didst raise him as if from sleep. * He shook off
                    corruption through the Spirit of incorruption, * and at Thy word he came out
                    bound with grave-clothes. * All things are possible to Thee, all things work for
                    Thee, O Lover of mankind, * all things submit to Thee: ** O Our Savior, glory
                    be to Thee.
            """
            ,'aposticha_theotokion': """
                    On the Aposticha, these Stichera in Tone VIII:
                    Having completed the spiritually profitable forty days, * we entreat Thee O
                    Lover of mankind: * Grant us also to behold the Holy Week of Thy Passion, *
                    that in it we may glorify Thy mighty acts * and Thine ineffable dispensation for
                    our sakes, * so that with one mind we may chant: ** “O Lord, glory be to Thee”.
                     Verse: Unto Thee have I lifted up mine eyes, unto Thee that dwellest in
                    heaven. Behold, as the eyes of servants look unto the hands of their
                    masters, as the eyes of the handmaid look unto the hands of her mistress,
                    so do our eyes look unto the Lord our God, * until He take pity on us.
                    Repeat: Having completed the forty days ...,
                    Verse: Have mercy on us, O Lord, have mercy on us, for greatly are we
                    filled with abasement. Greatly hath our soul been filled therewith; let
                    reproach come upon them that prosper, * and abasement on the proud.
                    Of the Martyrs, in Tone VIII:
                    O ye martyrs of the Lord, * pray ye on our behalf to God, * beseech Him to
                    grant abundant mercy to our souls ** and the forgiveness of our many
                    transgressions.
                    Glory ..., Now & Ever ..., in Tone VIII:
                    Standing before the tomb of Lazarus, O our Savior, * and having called out
                    to the dead man, * Thou didst raise him as if from sleep. * He shook off
                    corruption through the Spirit of incorruption, * and at Thy word he came out
                    bound with grave-clothes. * All things are possible to Thee, all things work for
                    Thee, O Lover of mankind, * all things submit to Thee: ** O Our Savior, glory
                    be to Thee.
            """
        } #Vespers
        ,'matins': {
            'troparion': """
                Troparion of the day, in Tone I:
                In confirming the common Resurrection, O Christ God, * Thou
                didst raise up Lazarus from the dead before Thy passion. * Wherefore, we also,
                like the children bearing the symbols of victory, * cry to Thee, the Vanquisher of
                death: * Hosanna in the highest; ** blessed is He that cometh in the name of the
                Lord. (Twice)
            """
            ,'evlogitaria':"""
                The Resurrectional Verses (THE EVLOGITARIA)
                Blessed art Thou, O Lord, * teach me Thy statutes.
                The assembly of angels was amazed, * beholding Thee numbered among the
                dead; * yet, O Savior, * destroying the stronghold of death, * and with Thyself
                raising up Adam, ** Thou hast freed all from Hades.
                Blessed art Thou, O Lord, * teach me Thy statutes.
                Why mingle ye myrrh with tears of pity, * O ye women disciples? * Thus said
                the radiant angel within the tomb * addressing the myrrh-bearing women; *
                behold the tomb and understand, ** for the Savior hath arisen from the tomb.
                Blessed art Thou, O Lord, * teach me Thy statutes.
                Very early * the myrrh-bearing women hastened * unto Thy tomb, lamenting,
                * but the angel stood before them and said: * the time for lamentation is passed,
                weep not, ** but tell the apostles of the Resurrection.
                Blessed art Thou, O Lord, * teach me Thy statutes.
                The myrrh-bearing women, * with myrrh came to Thy tomb, O Savior,
                bewailing, * but the angel addressed them, saying: * Why number ye the living
                among the dead, * for as God ** He is risen from the tomb.
                Glory to the Father, and to the Son, and to the Holy Spirit.
                Let us worship the Father, * and His Son, and the Holy Spirit, * the Holy
                Trinity, * one in essence, * crying with the Seraphim: ** Holy, Holy, Holy art
                Thou, O Lord.
                Both Now and ever, and unto the ages of ages, Amen..
                In bringing forth the Giver of life, * thou hast delivered Adam from sin, O
                Virgin, * and hast brought joy to Eve * instead of sorrow; * and those fallen
                from life * have thereunto been restored, ** by Him Who of thee was incarnate,
                God and man.
            """
            ,'canon': """
                ODE I
                First Canon; by Theophanes, in Tone VIII:
                Irmos: Let us sing unto the Lord, * who led His people through the Red
                Sea: * for He alone hath gloriously been glorified.
                Refrain: Glory to Thee O God, Glory to Thee.
                Thou didst raise the dead Lazarus by Thy divine command; for Thou art the
                Fashioner and Guardian of Life, O Lover of mankind.
                Refrain: Glory to Thee O God, Glory to Thee.
                By Thy word Thou didst raise Lazarus, who was four days dead O immortal
                Lord, and by Thy might Thou hast destroyed the dark kingdom of Hades.
                Refrain: Glory to Thee O God, Glory to Thee.
                Unto all hast Thou given proof of Thy transcendent Divinity, O Master, by
                raising up Lazarus who was four days dead.
                Refrain: Glory to Thee O God, Glory to Thee.
                Today Bethany doth proclaim beforehand the Resurrection of Christ the
                Giver of Life, and it rejoiceth at the arising of Lazarus.
                Another Canon, by Kosmas the Monk, in Tone VIII:
                Irmos: Having passed through the Water ...,
                Refrain: Glory to Thee O God, Glory to Thee.
                In the beginning Thou didst bring forth all of creation from nothing, and as
                Master knowing the secrets of the heart, Thou didst foretell the falling asleep of
                Lazarus to Thy disciples.
                Refrain: Glory to Thee O God, Glory to Thee.
                O Christ, Thou hast assumed the nature of man, from the Virgin, and as a
                man Thou didst ask where Lazarus was buried, though as God Thou wast in no
                wise ignorant of this.
                Glory ..., Giving us an assurance of Thine own Resurrection, Thou didst raise
                Thy friend as if from sleep O Word, though he lay four days in the tomb and
                already stinketh.
                Now & ever ...,Theotokion: The hosts of angels and mankind ceaselessly
                hymn thee, O Unwedded Mother, for thou hast carried their Creator as a babe in
                thine arms.
                Katavasia: Having passed through the water as upon dry land, * and
                having escaped the malice of the Egyptians, * the Israelites cried aloud: *
                Unto our God and Redeemer let us sing.
                ODE III
                First Canon, in Tone VIII:
                Irmos: O Lord, thou art the confirmation of those who flee to Thee, *
                Thou art the Light of those in darkness, * and my spirit doth hymn Thee.
                Refrain: Glory to Thee O God, Glory to Thee.
                Displaying Thy two energies, O Savior, Thou didst manifest Thy two natures:
                for Thou art both God and man.
                Refrain: Glory to Thee O God, Glory to Thee.
                Though Thou art an Abyss of knowledge, Thou didst ask where the body of
                Lazarus had been laid. For it was Thy will, O Giver of Life, to raise him who lay
                there.
                Refrain: Glory to Thee O God, Glory to Thee.
                Passing from place to place, as a man, Thou didst appear, circumscribed; but,
                as God filling all things, Thou art uncircumscribed.
                Refrain: Glory to Thee O God, Glory to Thee.
                Lazarus arose, by Thy divine word, O Christ, I pray Thee, raise me also, who
                am deadened by my many sins.
                Second Canon, in Tone VIII:
                Irmos: O Lord, Creator of the vault of Heaven ...,
                Refrain: Glory to Thee O God, Glory to Thee.
                Standing in Bethany by the tomb of Lazarus, O wonderworking Lord, Thou
                didst shed tears for him in accordance with the law of nature, confirming that
                Thou hast indeed assumed flesh, O Jesus my God.
                Refrain: Glory to Thee O God, Glory to Thee.
                Straightway O Savior, in Thy sovereign authority, Thou didst assuage the
                sorrow of Mary and Martha, for Thou art the Resurrection, and life, as Thou
                didst say, for in truth Thou art the Lord of all.
                Glory ..., O Lord, from the ranks of the dead and the darkness of Hades hast
                thou snatched Thy friend Lazarus; by Thine all-powerful word breaking asunder
                the locked gates of the kingdom of death.
                Now & ever ..., Taking up Thy dwelling within the Virgin, O Lord, Thou
                didst appear to mankind in the flesh, that they may behold with their eyes Thee
                Who hast revealed her to be in truth the Theotokos and the support of the
                faithful, O only Lover of mankind.
                Katavasia: O Lord, Creator of the vault of Heaven * and Builder of the
                Church, * do Thou strengthen me in Thy love, O Summit of desire, * O
                Support of the faithful, * O only Lover of mankind.
                Sessional Hymn, in Tone IV:
                The sisters of Lazarus stood beside Christ together * and, weeping with bitter
                tears, * they said unto Him: “O Lord, Lazarus hath passed from us.” * And
                though as God He knew the place of burial, * as a man He asked them, *
                “Where have ye laid him?” * and coming upon the tomb, * He called out to
                Lazarus who was four days dead; ** and straightway he arose and worshipped
                the Lord who had raised him up.
                Glory ..., Now & ever ..., in Tone VIII:
                Foreseeing all things as the Creator, * Thou didst prophecy unto the
                disciples, saying: * “Our friend Lazarus hath fallen asleep today in Bethany.” *
                And, foreknowing the answer, Thou didst ask: * “Where have ye laid him?”, *
                while weeping as a man Thou didst pray unto the Father; * whereupon having
                called Lazarus whom Thou didst love, O Lord, * Thou didst raise him who had
                been four days dead, from the bowels of Hades. * Wherefore we cry unto Thee:
                * “Accept, O Christ our God, the praise we dare to offer unto Thee, ** and
                deem us all worthy of Thy glory”.
                ODE IV
                First Canon, in Tone VIII:
                Irmos: O Lord, I have heard the mystery of Thy dispensation; * I have
                considered Thy works, * and I have glorified Thy Divinity.
                Refrain: Glory to Thee O God, Glory to Thee.
                Not that Thou art in need of help, but in order to fulfill the inexpressible
                mystery of Thy plan; Praying, Thou didst raise up a corpse four days dead.
                Refrain: Glory to Thee O God, Glory to Thee.
                Coeternally existing with the Father, the Word Who hath been revealed from
                the beginning as God, now prayeth as a man, He Who accepteth the prayers of
                all.
                Refrain: Glory to Thee O God, Glory to Thee.
                O Savior, Thy voice hath destroyed all the power of death, and the
                foundations of Hades have been shaken by Thy Divinity.
                Refrain: Most Holy Theotokos save us.
                Let us hymn the Virgin, for she hath remained a virgin even after
                childbearing, having given birth to Christ God, Who hath delivered the world
                from delusion.
                Second Canon, in Tone VIII:
                Irmos: Thou, O Lord, art my strength ...,
                Refrain: Glory to Thee O God, Glory to Thee.
                O Savior and Creator, as Shepherd, Thou didst truly snatch the four day dead
                man from the wicked and all-devouring wolf; and through him O Lord, as allpowerful, Thou didst foreshadow the universal glory of Thy Resurrection on the
                third day.
                Refrain: Glory to Thee O God, Glory to Thee.
                Beholding Thee the Life, the companions of Martha cried aloud O Christ: “If
                Thou hadst been here, O Lord, Thou Light and Life of all, Lazarus would not
                have died.” But since Thou art the Life of the dead, O Lover of mankind Thou
                hast turned their sorrow into joy.
                Glory ..., O Lord Thou art the source of life, of Whom the depths quake in
                fear; for all the waters serve Thee, the gatekeepers of Hades tremble before Thee,
                O Christ, and the bars therein have been smashed by Thy power, and Lazarus
                hath been raised from the dead by Thy command, O almighty Savior, Lover of
                mankind.
                Now & ever ..., O unwedded Virgin, thou art the glory of the faithful; thou
                art the intercessor and refuge of Christians, their rampart and haven. For
                entreating thy Son O all-immaculate One, thou dost save from danger those who
                in faith and love acknowledge thee to be the pure Theotokos.
                Katavasia: Thou, O Lord, art my strength and Thou art my power, * Thou
                art my God and Thou art my joy, * Thou Who, while never leaving the
                bosom of Thy Father, * hast visited our poverty. * Therefore with the
                Prophet Habbakuk I cry unto Thee, * “Glory to Thy power, O Lover of
                mankind!”
                ODE V
                First Canon, in Tone VIII:
                Irmos: O Light never-waning, * why hast Thou turned Thy face from me *
                and why hath the alien darkness surrounded me, * wretched though I be?
                * But do Thou guide my steps I implore Thee * and turn me back towards
                the light of Thy commandments.
                Refrain: Glory to Thee O God, Glory to Thee.
                O Lover of mankind, having come to the tomb of Lazarus Thou, the
                immortal life of all mankind, didst call him and grant him life; whereby Thou, as
                God, hast clearly foreshadowed the future Resurrection.
                Refrain: Glory to Thee O God, Glory to Thee.
                His feet bound in grave-clothes, Lazarus walked forth from the tomb, O
                wonder of wonders! He who hath given him such strength is greater than the
                power which held him back, Christ, whose word all things obey, serving Him as
                God and Master.
                Refrain: Glory to Thee O God, Glory to Thee.
                O Christ, Thou Who didst raise Lazarus on the fourth day, raise me up also,
                who am deadened by my sins, and lie in the pit and the shadow of death; since
                Thou art exceedingly compassionate, deliver me and save me.
                Second Canon, in Tone VIII:
                Irmos: O Light never-waning ...,
                Refrain: Glory to Thee O God, Glory to Thee.
                Thou didst give glory to the Father, for Thy prayer was not a rebuke of God,
                but the confirmation of the faith of the multitude that stood around Thee, for
                Thou didst thank Thy Father, O longsuffering Lord, and then raise Lazarus by
                Thy command.
                Refrain: Glory to Thee O God, Glory to Thee.
                O divine voice of God’s proclamation! O divine power and might! With
                which, O Savior, Thou hast shattered the gates of Hades and its all-devouring
                death. Deliver me from my passions, as Thou didst once deliver Thy four day
                dead friend Lazarus.
                Glory ..., By the prayers of Lazarus, and of Martha and Mary, deem us worthy
                to behold Thy Cross and Passion, and the joyful light-bearing Queen of Days,
                the Feast of Thy Resurrection, O Lover of mankind.
                Now & ever ..., O most pure one, since thou hast a mother’s boldness before
                thy Son, forget not us who are in need, we pray thee, for we are thy kinsfolk:
                thee alone do we Christians offer as an intercessor, to win the Master’s favor.
                Katavasia: O Light never-waning, * why hast Thou turned Thy face from
                me * and why hath the alien darkness surrounded me, * wretched though
                I be? * But do Thou guide my steps I implore Thee * and turn me back
                towards the light of Thy commandments.
                Note: We now begin the two four-canticled Canons. The Irmos of the
                first Canon is sung twice, and the Troparia of the two Canons are then
                repeated so as to make up the number twelve.
                ODE VI
                First Canon, by Kosmas the Monk, in Tone VIII:
                Irmos: Thou O Lord, didst place Jonah alone within the sea monster. * Do
                Thou save me, * who am ensnared in the nets of the enemy, * as thou
                didst save him from corruption.
                Refrain: Glory to Thee O God, Glory to Thee.
                Love led Thee, O Lord, to Lazarus in Bethany; and as God, even though his
                corpse did stink, Thou didst raise him up, and save him from the bonds of
                Hades.
                Refrain: Glory to Thee O God, Glory to Thee.
                Martha despaired when she saw Lazarus already four days dead. But Christ,
                as God, raised him from the decay of corruption and brought him back to life by
                His word.
                Another Canon, by John the Monk, in Tone VIII:
                Irmos: Cleanse me, O Savior ...,
                Refrain: Glory to Thee O God, Glory to Thee.
                As the true God Thou didst foreknow the falling asleep of Lazarus and
                having announced it beforehand to Thy disciples, Thou didst confirm in them, O
                Master, the recognition of the infinite Power of Thy divinity.
                Glory ..., Now & ever ..., Thou who by nature art uncircumscribed, wast
                circumscribed in the flesh; and coming to Bethany, O Master, as a man Thou
                didst weep over Lazarus, but as God Thou didst, by Thy will, raise up him who
                was four days dead.
                Katavasia: Cleanse me, O Savior, * for many are mine iniquities; *
                lead me up from the abyss of evils I pray Thee, * for unto Thee have I
                cried, * and Thou hast hearkened unto me, * O God of my salvation.
                Kontakion, in Tone II:
                Christ, the joy of all, * the truth, the light, the life, the resurrection of the
                world, * in His loving-kindness hath appeared unto those on earth; * and became
                the prototype of our resurrection, ** granting unto all divine forgiveness.
                Ikos: The Creator of the world foretold His disciples that which came to
                pass, proving to them that as the Creator of all things He is all-knowing.
                “Brethren and companions, our friend hath fallen asleep”, He said. “Let us go,
                then, and see a strange burial, and behold the tears of Mary and the tomb of
                Lazarus. For I shall work a miracle there, as the prelude to my Crucifixion,
                granting divine forgiveness unto all.
                SYNAXARION READING
                Verse: Lamenting O Jesus, over him who had reposed.
                Verse: Thou didst bring to life Thy friend, by Thy divine might.
                On this day, the Saturday before Palm Sunday, we celebrate the fourth-day
                raising from the dead of Lazarus, the righteous friend of Christ. Lazarus was a
                Hebrew, of the sect of the Pharisees and, as far as is known, he was the son of
                Simon the Pharisee, who dwelt in the village of Bethany. He became a friend of
                our Lord Jesus Christ when He sojourned on earth for the salvation of our race.
                For when Christ continually conversed with Simon, entering his house and
                discoursing on the resurrection from the dead, Lazarus was quite pleased with
                the genuineness of this teaching, and not only he, but also his two sisters, Martha
                and Mary. As the time of the Savior’s Passion drew near, when it was especially
                necessary to believe in the Mystery of the Resurrection, Jesus was sojourning on
                the other side of the Jordan. Here, He raised from the dead the daughter of
                Jairus and the son of the widow. At this time, His friend, Lazarus, contracted a
                grievous illness and died. Then Jesus, even though He was not present there, said
                to His disciples, Our friend Lazarus sleepeth; but I go, that I may awake him out
                of sleep (John 11:11), and again a little later, Lazarus is dead. (See John 11:14.)
                Then Jesus left the Jordan and went to Bethany, which was about fifteen stadia
                (approximately 2 miles) away from Jerusalem. Martha, the sister of Lazarus, went
                to meet Him and said, Lord, if thou hadst been here, my brother had not died.
                But I know, that even now, whatsoever thou wilt ask of God, God will give it
                thee. (John 11:21-22). Jesus asked the crowd, Where have ye laid him? (John
                11:34.) Immediately everyone went to the tomb. As the stone was removed,
                Martha said, Lord, by this time he stinketh: for he hath been dead four days.
                (John 11:39). He shed tears for the one lying there, and He cried out with a loud
                voice, Lazarus, come forth (John 11:43). At once, he who was dead came forth,
                was unbound, and set out for home amidst great rejoicing and thanksgiving. This
                strange wonder roused the Hebrew people to malice, and they were infuriated
                with Christ. But Jesus once more fled and escaped. The high priests determined
                to kill Lazarus, because many who saw him were won over to Christ. Since
                Lazarus knew what they were thinking, he sailed away to Cyprus. He dwelt there
                and was later elevated by the Holy Apostles to be Archbishop of Citium
                (present-day Larnaka). He was beloved by God, conducting himself most nobly
                as an archpastor, performing many miracles. Thirty years after his resurrection, in
                63 A.D., he died once more and was buried in Citium. It is said that after his
                return to life Lazarus ate only meals having some sweetness, because of the bitter
                taste in his mouth from having been dead. Also, it is related that the Most holy
                Mother of God sewed his omophorion and cuffs with her own hands and
                presented them to him as a gift. Furthermore, it is told that Lazarus never
                laughed more than once after being raised from the dead, and that was when he
                observed someone stealing a clay vessel. At that point he smiled and said, “Clay
                stealing clay.” Lazarus said nothing concerning those in Hades, either because he
                was not permitted to behold anything, or he was directed to be silent about what
                he had seen. The most wise emperor Leo, in 890 A.D., after a divine vision,
                transported the precious and holy relics of this saint to Constantinople to the
                church of St. Lazarus that he had constructed and deposited them reverently and
                ceremoniously to the right of the church’s entrance against the front walls of the
                holy bema. Here his precious relics still remain, exuding an ineffable fragrance.
                The translation of his holy relics is commemorated on October 17. The
                resurrection of Lazarus is appointed to be celebrated on this present day, after
                the forty-day purifying Fast, because our Holy and God-bearing Fathers,
                especially the Holy Apostles, found this miracle to be the beginning and cause of
                the fury of the Jews against Christ, when He was about to give Himself over to
                His Holy Sufferings. For this reason they placed this extraordinary and
                wonderful event here. In addition, the placement of this feast by the Holy
                Fathers serves as a necessary rest” and “transition” between the rigors of the
                Fast and the awesome and saving events of Holy Week. For in truth, yesterday
                evening’s Vespers not only ended the Holy Forty Days, but also ushered us into
                a joyous Resurrectional prelude that will eventually lead to our Savior’s Passion.
                St. John the Theologian alone records the raising of Lazarus, since the other
                Evangelists omitted it—perhaps because Lazarus was still living and able to be
                seen. It is said that the rest of the Gospel of John was written about the eternal
                begotteness of Christ, the other Evangelists including nothing about this. It is
                desired to believe that Christ is both the Son of God and God, that He is risen,
                and that there will be a resurrection of the dead. And because of the raising of
                Lazarus, this is especially to be believed since his resurrection is a confirmation
                of the universal resurrection of man. Therefore, from this event, every man who
                has already died is said to be a “Lazarus,” and the burial garment is called a
                Lazaroma, for the word alludes to the remembrance of the first Lazarus. For if
                Lazarus was raised by the word of Christ and came back to life again, so all men,
                even if they have died, will rise at the last trumpet and live eternally.
                Through the intercessions of Thy beloved friend, St. Lazarus,
                О Christ our God, have mercy on us and save us. Amen.
                ODE VII
                First Canon, in Tone VIII:
                Irmos: The Hebrew children in the furnace * boldly trampled upon the
                flames, * changing the fire into dew, they cried aloud: * “Blessed art
                Thou, O Lord our God, throughout the ages”.
                Refrain: Glory to Thee O God, Glory to Thee.
                As a man Thou didst weep O compassionate One, but as God Thou didst
                raise Lazarus from the tomb; and having been delivered from Hades, he cried
                aloud: “Blessed art Thou, O Lord God, throughout the ages.”
                Refrain: Glory to Thee O God, Glory to Thee.
                Coming forth bound in grave clothes, and fleeing from the chaos and
                darkness of Hades, by the Master’s word, Lazarus cried aloud: “Blessed art Thou,
                O Lord God, throughout the ages.”
                Second Canon, in Tone VIII:
                Irmos: The Children of Judaea ...,
                Refrain: Glory to Thee O God, Glory to Thee.
                Shedding tears over Thy friend, O Compassionate One, Thou didst assuage
                the tears of Martha, and by Thy voluntary Passion Thou didst wipe away all tears
                from the face of Thy people. O God of our fathers, blessed art Thou.
                Glory ..., O Treasury of life, Thou didst raise him who was dead, as if from
                sleep, by Thy word bursting asunder the belly of Hades, and having arisen he
                chanted: “O God of our fathers, blessed art Thou.”
                Now & ever ..., A stinking corpse, and one bound in grave clothes hast Thou
                raised up O Master, raise me also who am held fast in the bonds of sin that I may
                sing: “O God of our fathers, blessed art Thou”.
                Katavasia: The Children of Judaea, * who of old came to dwell in Babylon,
                * trampled underfoot the flame of the furnace * through their faith in the
                Trinity, * as they sang: “O God of our fathers, blessed art Thou.”
                ODE VIII
                First Canon, in Tone VIII:
                Irmos: The instruments of music sounded out in harmony, * and
                countless multitudes worshipped the image in Dura; * but the three
                Children, refusing to bow in obeisance, * hymn and glorify the Lord
                throughout all ages.
                Refrain: Glory to Thee O God, Glory to Thee.
                Like a Shepherd, Thou didst seek Thy lamb, rescuing him from the wicked
                and destructive wolf, and restoring him who had fallen into corruption,
                wherefore he cried out to Thee: “Praise ye, and supremely exalt Him throughout
                all ages.”
                Refrain: Glory to Thee O God, Glory to Thee.
                As a man Thou didst ask where Lazarus was buried; as the Fashioner, Thou
                didst raise him from the dead, by Thy royal command, which Hades feared as he
                cried out to Thee: “Praise ye, and supremely exalt Him throughout all ages.”
                Second Canon, in Tone VIII:
                Irmos: The King of heaven ...,
                Refrain: Glory to Thee O God, Glory to Thee.
                As a mortal, Thou didst seek out Lazarus, as God, Thou didst raise him who
                was four days dead by Thy word, wherefore we hymn, and supremely exalt Thee
                throughout all ages.
                We bless the Father, Son, and Holy Spirit, the Lord.
                Fulfilling a debt of gratitude on behalf of her brother, Mary brought Thee, O
                Lord, sweet-smelling spices, hymning Thee throughout all ages.
                Now & ever ..., As a man Thou dost call out to the Father, as God Thou
                dost raise Lazarus, wherefore, we hymn Christ throughout the ages.
                We praise, bless and worship the Lord ...,
                Katavasia: The King of heaven, * Who is glorified by the hosts of angels, *
                let us praise and supremely exalt throughout all ages.
                (We do not chant the Magnificat)
                ODE IX
                First Canon, in Tone VIII:
                Irmos: O ye people, with glory let us honor the pure Theotokos, * who
                received the fire of the Divinity in her womb * yet remained unconsumed,
                * let us magnify her with hymns.
                Refrain: Glory to Thee O God, Glory to Thee.
                Having seen a four-day dead corpse walking, the people were struck with
                wonder at the miracle and cried out to the Redeemer: “In hymns do we magnify
                Thee, O God.”
                Refrain: Glory to Thee O God, Glory to Thee.
                Thou didst confirm faith in Thy glorious Resurrection, O my Savior, before it
                came to pass, by freeing him who was four days dead from Hades, wherefore in
                hymns I magnify Thee.
                Second Canon, in Tone VIII:
                Irmos: Saved by thee, O pure Virgin ...,
                Refrain: Glory to Thee O God, Glory to Thee.
                Honoring Thy Father, O Christ, and showing that in no way art Thou
                opposed to Him, upon praying, and by Thine own authority, Thou didst raise
                him who was four days dead.
                Refrain: Glory to Thee O God, Glory to Thee.
                Thou didst raise from the tomb Lazarus who was four days dead, thereby
                making him a most truthful witness, O Christ, to Thy Resurrection on the third
                day.
                Glory ..., Thou dost walk, and weep, and speak, O my Savior, showing the
                activity of Thy human nature; and Thou didst raise Lazarus, revealing Thy divine
                nature.
                Now & ever ..., In ways inexpressible, O my Master and Savior, and in
                accordance with the free-will exercised in each of Thy two natures, Thou hast
                brought about my salvation.
                Katavasia: Saved by thee, O pure Virgin, * we confess thee to be truly the
                Theotokos, * and together with the choirs of the bodiless hosts * thee do
                we magnify.
            """
            ,'exapostilarion': """
                Exapostilarion, in Tone III:
                By Thy word, O Word of God, Lazarus now leapeth up, * returning back to
                life, * wherefore the people honor Thee with palms, * O mighty Lord, ** for by
                Thy death Thou shalt utterly destroy Hades (Twice).
                Glory ..., Now & ever ..., in Tone III:
                Through Lazarus, O death, Christ hath already despoiled thee. * O Hades,
                where is thy victory? * The lamentation of Bethany hath now been presented to
                thee. * In Christ’s honor let us raise on high ** the branches of victory.
            """
            ,'praises':"""
                On the Praises, 8 Stichera, 4 Stichera in Tone I:
                Verse: To do among them the judgment that is written * This glory shall
                be to all His saints.
                Thou art the Resurrection and the Life of mankind, O Christ, * standing by
                the tomb of Lazarus * Thou hast confirmed our faith in Thy two natures, O
                longsuffering Lord, * proving that Thou didst come forth from the pure Virgin *
                as both God and man. * For as a man Thou didst ask, * “Where is he buried?” *
                and as God by Thy life-giving command ** Thou didst raise him from the dead
                on the fourth day.
                Verse: Praise ye God in His saints, * praise Him in the firmament of His
                power.
                Before Thine own death, O Christ, * Thou didst raise the four days dead
                Lazarus from Hades, * thereby shaking the dominion of death. * By this one
                man loved by Thee, * Thou hast foretold the deliverance of all mankind from
                corruption. * We therefore worship Thine almighty power and cry aloud: **
                “Blessed art Thou, O Savior, have mercy on us”.
                Verse: Praise Him for His mighty acts, * praise Him according to the
                multitude of His greatness.
                Martha and Mary spake to the Savior saying: * “Hadst Thou, O Lord, been
                here, * Lazarus would not have died.” * But Christ, the Resurrection of those
                who have reposed, * hath raised from the dead, him who was four days dead. *
                Draw near, O ye faithful, * and let us all worship Him ** who cometh in glory to
                save our souls.
                Verse: Praise Him with the sound of trumpet, * praise Him with the
                psaltery and harp.
                Thou didst grant unto Thy disciples, O Christ, * proofs of Thy divinity, * but
                among the crowds Thou didst humble Thyself, * wishing to conceal this from
                them. * As God, foreseeing all things, Thou didst foretell the death of Lazarus to
                the apostles; * yet at Bethany, when in the presence of the people, * as a man
                Thou didst ask where Thy friend was buried, * not in any way ignorant of this, *
                But having raised him four days after he had died, * Thou didst manifest Thy
                power as God. ** O almighty Lord, glory be to Thee.
                Two Stichera in Tone IV:
                Verse: Praise Him with timbrel and dance, * praise him with strings and
                flute.
                O Christ, Thou didst raise up Thy four days dead friend, * thereby assuaging
                the lamentation of Martha and Mary, * showing to all that Thou art He who
                fillest all things * by Thy divine power and Thy sovereign will. * Unto Whom the
                cherubim without ceasing cry aloud: * “Hosanna in the highest: ** blessed art
                Thou, O God of all: glory be to Thee.”
                Verse: Praise Him with tuneful cymbals, praise Him with cymbals of
                jubilation. * Let every breath praise the Lord.
                Martha cried to Mary: * “Come, the Teacher standeth here and calleth for
                thee:.” * And she, running to the place where Thou wast O Lord, * she cried out
                when she saw Thee; * and falling at Thy feet she worshipped Thee, saying: ** “O
                Lord, hadst Thou been here, our brother had not died. “
                Then two Stichera in Tone VIII:
                Verse: Arise, O Lord my God, let Thy hands be lifted high; * forget not
                Thy paupers to the end.
                Thou didst raise up Lazarus who had reposed in Bethany * and was four days
                dead; * For as soon as Thou didst stand by the tomb, * The sound of Thy voice
                became the source of life to him who had reposed, * and Hades groaning aloud,
                released him in fear. * O mighty miracle! ** O abundantly merciful Lord, glory
                be to Thee.
                Verse: I will confess Thee, O Lord, with my whole heart, * I will tell of all
                Thy wonders.
                O Lord, Thou didst say to Martha, * “I am the Resurrection”; * and Thou
                hast confirmed Thy Words by Thy deeds, * calling Lazarus from Hades, *
                wherefore I beseech Thee; * do Thou raise me up who am also deadened by my
                passions, ** since Thou art the Lover of mankind.
                Glory ..., in Tone II:
                A great and marvelous wonder hath been wrought today: * for calling to a
                four-day dead corpse, * Christ hath raised His friend from the tomb. * Let us
                glorify Him, for He is supreme in glory, * that by the prayers of righteous
                Lazarus ** He may save our souls.
                Now & ever ..., in Tone II:
                Most Blessed art Thou, O Virgin Theotokos, * for through Him Who
                became incarnate of thee is Hades led captive, * Adam recalled, the curse
                annulled, Eve set free, death slain, * and we are given life. Wherefore, we cry
                aloud in praise: * Blessed art Thou, O Christ God, ** Who hast been thus wellpleased, glory be to Thee.
            """
        } #Matins
        ,'liturgy': {
            'beatitudes': [
                """
                    Displaying Thy two energies, O Savior, Thou didst manifest Thy two natures:
                    for Thou art both God and man.
                """
                ,"""
                    Though Thou art an Abyss of knowledge, Thou didst ask where the body of
                    Lazarus had been laid. For it was Thy will, O Giver of Life, to raise him who lay
                    there.
                """
                ,"""
                    Passing from place to place, as a man, Thou didst appear, circumscribed; but,
                    as God filling all things, Thou art uncircumscribed.
                """
                ,"""
                    Lazarus arose, by Thy divine word, O Christ, I pray Thee, raise me also, who
                    am deadened by my many sins.
                """
                ,"""
                    As the true God Thou didst foreknow the falling asleep of Lazarus and
                    having announced it beforehand to Thy disciples, Thou didst confirm in them, O
                    Master, the recognition of the infinite Power of Thy divinity.
                """
                ,"""
                    As the true God Thou didst foreknow the falling asleep of Lazarus and
                    having announced it beforehand to Thy disciples, Thou didst confirm in them, O
                    Master, the recognition of the infinite Power of Thy divinity.
                """
                ,"""
                    Thou who by nature art uncircumscribed, wast circumscribed in the flesh;
                    and coming to Bethany, O Master, as a man Thou didst weep over Lazarus, but
                    as God Thou didst, by Thy will, raise up him who was four days dead.
                """
                ,"""
                    Thou who by nature art uncircumscribed, wast circumscribed in the flesh;
                    and coming to Bethany, O Master, as a man Thou didst weep over Lazarus, but
                    as God Thou didst, by Thy will, raise up him who was four days dead.
                """
            ]
            ,'troparion':"""
                The Troparion of the day, in Tone I:
                In confirming the common Resurrection, O Christ God, * Thou
                didst raise up Lazarus from the dead before Thy passion. * Wherefore, we also,
                like the children bearing the symbols of victory, * cry to Thee, the Vanquisher of
                death: * Hosanna in the highest; ** blessed is He that cometh in the name of the
                Lord.
            """
            ,'kontakion': """
                The Kontakion of the day, in Tone II:
                Christ, the joy of all, * the truth, the light, the life, the resurrection of the
                world, * in His loving-kindness hath appeared unto those on earth; * and became
                the prototype of our resurrection,** granting unto all divine forgiveness.
            """
            ,'prokeimenon':"""
                Prokeimenon: The Lord is my Light and my Savior: * Whom then shall I
                fear?
                Verse: The Lord is the defender of my life: of whom then shall I be
                afraid?
            """
            ,'readings': """

            """
        } #Liturgy
    } #Service
    ,'-7': { #Palm Sunday
        'vespers': {
            'stichera_tone': 'in Tone VI:'
            ,'stichera': [
                """
                    Today the grace of the Holy Spirit * hath gathered us together, * and having
                    taken up Thy Cross, we all say: * “Blessed is He that cometh in the Name of the
                    Lord; ** Hosanna in the highest”.
                """
                ,"""
                    Today the grace of the Holy Spirit * hath gathered us together, * and having
                    taken up Thy Cross, we all say: * “Blessed is He that cometh in the Name of the
                    Lord; ** Hosanna in the highest”.
                """
                ,"""
                    He whose throne is the heavens and * and whose footstool is the earth, *
                    the co-eternal Word and Son of God the Father, * hath humbled Himself today
                    and come to Bethany, * seated upon the foal of an ass, * wherefore the children
                    of the Hebrews, * holding branches in their hands, * praise Him saying:
                    “Hosanna in the highest: ** Blessed is He that cometh, the King of Israel.”
                """
                ,"""
                    He whose throne is the heavens and * and whose footstool is the earth, *
                    the co-eternal Word and Son of God the Father, * hath humbled Himself today
                    and come to Bethany, * seated upon the foal of an ass, * wherefore the children
                    of the Hebrews, * holding branches in their hands, * praise Him saying:
                    “Hosanna in the highest: ** Blessed is He that cometh, the King of Israel.”
                """
                ,"""
                    Let us also come today, * all the new Israel, the Church of the Gentiles, *
                    and let us cry with the Prophet Zechariah: * Rejoice greatly, O daughter of Zion;
                    * extol in praise, O daughter of Jerusalem; * for behold, thy King cometh unto
                    thee, meek and bearing salvation, * seated upon the colt of an ass, * the foal of a
                    beast of burden. * Keep ye the feast with the children, * and holding branches in
                    your hands * sing His praises: * “Hosanna in the highest; ** blessed is He that
                    cometh, the King of Israel”.
                """
                ,"""
                    Let us also come today, * all the new Israel, the Church of the Gentiles, *
                    and let us cry with the Prophet Zechariah: * Rejoice greatly, O daughter of Zion;
                    * extol in praise, O daughter of Jerusalem; * for behold, thy King cometh unto
                    thee, meek and bearing salvation, * seated upon the colt of an ass, * the foal of a
                    beast of burden. * Keep ye the feast with the children, * and holding branches in
                    your hands * sing His praises: * “Hosanna in the highest; ** blessed is He that
                    cometh, the King of Israel”.
                """
                ,"""
                    Prefiguring for us Thy holy Resurrection, * Thou didst raise up by Thy
                    command Thy deceased friend Lazarus, O Good One, * who lay four days in the
                    tomb without the breath of life and reeking of death; * After which, mounted
                    upon a foal, as though carried by a chariot O Savior, * Thou didst give an
                    example of meekness to the Gentiles. * wherefore also Israel Thy beloved, offers
                    Thee praise * out of the mouth of babes and sucklings, * as they behold Thee,
                    Christ, enter the Holy City ** six days before the Passover.
                """
                ,"""
                    Prefiguring for us Thy holy Resurrection, * Thou didst raise up by Thy
                    command Thy deceased friend Lazarus, O Good One, * who lay four days in the
                    tomb without the breath of life and reeking of death; * After which, mounted
                    upon a foal, as though carried by a chariot O Savior, * Thou didst give an
                    example of meekness to the Gentiles. * wherefore also Israel Thy beloved, offers
                    Thee praise * out of the mouth of babes and sucklings, * as they behold Thee,
                    Christ, enter the Holy City ** six days before the Passover.
                """
                ,"""
                    Six days before the Passover Jesus hath entered Bethany, * and His disciples
                    came up to Him, saying: * “O Lord, where wilt Thou that we prepare for Thee to
                    eat the Passover?” * He then sent them, saying: * “Go ye into the village
                    opposite, * and there ye shall find a man bearing a pitcher of water; * follow him,
                    and tell the master of the house: * The Teacher hath said, In thy house shall I eat
                    the Passover ** with My disciples.”
                """
                ,"""
                    Six days before the Passover Jesus hath entered Bethany, * and His disciples
                    came up to Him, saying: * “O Lord, where wilt Thou that we prepare for Thee to
                    eat the Passover?” * He then sent them, saying: * “Go ye into the village
                    opposite, * and there ye shall find a man bearing a pitcher of water; * follow him,
                    and tell the master of the house: * The Teacher hath said, In thy house shall I eat
                    the Passover ** with My disciples.”
                """
            ]
            ,'doxastichon': """
                in Tone VI:
                Today the grace of the Holy Spirit * hath gathered us together, * and having
                taken up Thy Cross, we all say: * “Blessed is He that cometh in the Name of the
                Lord; ** Hosanna in the highest”.
            """
            ,'readings':"""
                READING FROM THE BOOK OF GENESIS (49: 1-2, 8-12)
                And Jacob called unto his sons, and said, Gather yourselves together, that I
                may tell you that which shall befall you in the last days. Gather yourselves
                together, and hear, ye sons of Jacob; and hearken unto Israel your father. Judah,
                thou art he whom thy brethren shall praise: thy hand shall be in the neck of thine
                enemies; thy father’s children shall bow down before thee. Judah is a lion’s
                whelp: from the prey, my son, thou art gone up: he stooped down, he couched as
                a lion, and as an old lion; who shall rouse him up? The sceptre shall not depart
                from Judah, nor a lawgiver from between his feet, until Shiloh come; and unto
                him shall the gathering of the people be. Binding his foal unto the vine, and his
                ass’s colt unto the choice vine; he washed his garments in wine, and his clothes in
                the blood of grapes: His eyes shall be red with wine, and his teeth white with
                milk.
                READING FROM THE PROPHECY OF ZEPHANIAH (3:14-19)
                Thus saith the Lord: Rejoice, O daughters of Zion; shout, O Israel; be glad
                and rejoice with all the heart, O daughters of Jerusalem. The LORD hath taken
                away thy judgments, he hath cast out thine enemy: the king of Israel, even the
                LORD, is in the midst of thee: thou shalt not see evil any more. In that day it
                shall be said to Jerusalem, Fear thou not: and to Zion, Let not thine hands be
                slack. The LORD thy God in the midst of thee is mighty; he will save, he will
                rejoice over thee with joy; he will rest in his love, he will joy over thee with
                singing. I will gather them that are sorrowful for the solemn assembly, who are
                of thee, to whom the reproach of it was a burden. Behold, at that time I will
                undo all that afflict thee: and I will save her that halteth, and gather her that was
                driven out; and I will get them praise and fame in every land where they have
                been put to shame.
                READING FROM THE PROPHECY OF ZECHARIAH (9:9-15)
                Thus saith the Lord: Rejoice greatly, O daughter of Zion; shout, O daughter
                of Jerusalem: behold, thy King cometh unto thee: he is just, and having salvation;
                lowly, and riding upon an ass, and upon a colt the foal of an ass. And I will cut
                off the chariot from Ephraim, and the horse from Jerusalem, and the battle bow
                shall be cut off: and he shall speak peace unto the heathen: and his dominion
                shall be from sea even to sea, and from the river even to the ends of the earth.
                As for thee also, by the blood of thy covenant I have sent forth thy prisoners out
                of the pit wherein is no water. Turn you to the strong hold, ye prisoners of hope:
                even to day do I declare that I will render double unto thee; When I have bent
                Judah for me, filled the bow with Ephraim, and raised up thy sons, O Zion,
                against thy sons, O Greece, and made thee as the sword of a mighty man. And
                the LORD shall be seen over them, and his arrow shall go forth as the lightning:
                and the LORD God shall blow the trumpet, and shall go with whirlwinds of the
                south. The LORD of hosts shall defend them.
            """
            ,'litiya':"""
                in Tone I:
                The all-holy Spirit, * Who taught the apostles to speak in strange tongues, *
                now inspireth the innocent children of the Hebrews to cry aloud: * “Hosanna in
                the highest; ** blessed is He that cometh, the King of Israel”.
                The co-beginningless and co-eternal Son and Word of the Father, * seated
                on a dumb beast, the foal of an ass, * hath come today to the city of Jerusalem, *
                He whom the cherubim dare not gaze upon from fear; * do the children honor
                with palms and branches, * mystically singing a hymn of praise: * “Hosanna in
                the highest, * Hosanna to the Son of David, ** Who hath come to save all
                mankind from deception.”
                Six days before the Passover, O Lord, * Thy voice was heard in the depths
                of Hades, * from whence Thou didst raise up Lazarus who was four days dead. *
                and the children of the Hebrews cried aloud: ** “Hosanna to our God: Glory be
                to Thee!”
                Tone II: Entering, O Lord, into the Holy City, seated upon a foal, * Thou
                didst draw near with haste unto Thy Passion, * to fulfill the Law and the
                Prophets. * The children of the Hebrews, foretelling the victory of the
                Resurrection, * came to meet Thee with palms and branches, saying: ** “Blessed
                art Thou, O Savior; have mercy on us.”
                Glory be to Thee, O Christ, * Who art seated in the heights upon Thy
                throne, * and whom we now await with Thy precious Cross. * Wherefore the
                daughter of Zion is gladdened, * and the nations of the earth rejoice. * and the
                children hold branches, and the disciples spread their garments in the way; * and
                all the inhabited earth hath been taught to cry aloud: ** “Blessed art Thou, O
                Savior; have mercy on us”.
                Glory ..., Now & Ever ..., in Tone III:
                Six days before the Passover Jesus came to Bethany, * to call back Lazarus
                who was four days dead, * and to preach of the coming Resurrection. * The
                women, Martha and Mary, the sisters of Lazarus, * came to meet Him, crying to
                Him: “Lord, if Thou hadst been here, our brother had not died.” * Then He
                answered them: “Did I not say to you before: * He who believeth in Me, though
                he be dead, yet shall he live? * Show Me where ye have laid him.” ** And the
                Maker of all cried unto him, “Lazarus, come forth.”
            """
            ,'aposticha':"""
                in Tone VIII:
                Rejoice and be glad, O city of Zion; * exult and be exceedingly joyful, O
                Church of God. * For behold, thy King hath come in righteousness, seated on a
                foal, * and the children sing His praises: * “Hosanna in the highest! * Blessed art
                Thou Who art abundantly compassionate: ** Have mercy on us”.
                Verse: Out of the mouth of babes and sucklings * hast Thou perfected
                praise.
                The Savior hath come today to the city of Jerusalem, * to fulfill the
                Scriptures; * and all have taken palms in their hands * and spread their garments
                before Him, * knowing that He is our God, * unto whom the cherubim without
                ceasing sing: * “Hosanna in the highest! * Blessed art Thou Who art abundantly
                compassionate: ** Have mercy on us”.
                Verse: O Lord, our Lord, how wonderful is Thy Name * in all the
                earth.
                Thou Who art seated upon the cherubim and praised by the seraphim, *
                wast seated, O gracious Lord, like David upon a foal, * and the children praised
                Thee in godly manner; * but the Jews unlawfully blasphemed against Thee, * thus
                prefiguring the manner by which the Gentiles, * as yet untamed and
                uninstructed, * were to pass from unbelief to faith. * Glory be to Thee, O Christ,
                ** Who alone art merciful and lovest mankind.
            """
            ,'aposticha_theotokion': """
                in Tone VI:
                Today the grace of the Holy Spirit * hath gathered us together, * and we all
                take up Thy Cross and say: * Blessed is He that cometh in the Name of the Lord;
                ** Hosanna in the highest.
            """
        } #Vespers
        ,'matins': {
            'troparion': """
                in Tone I:
                In confirming the common Resurrection, O Christ God, * Thou
                didst raise up Lazarus from the dead before Thy passion. * Wherefore, we also,
                like the children bearing the symbols of victory, * cry to Thee, the Vanquisher of
                death: * Hosanna in the highest; ** blessed is He that cometh in the name of the
                Lord.
                Glory ..., Now & Ever ..., Another Troparion, in Tone IV:
                As by baptism we were buried with Thee, O Christ our God, * so by Thy
                Resurrection we were deemed worthy of immortal life; * and praising Thee, we
                cry: * Hosanna in the highest; ** blessed is He that cometh in the name of the
                Lord.
            """
            ,'after50': """
                Glory ..., in Tone II:
                Today Christ entereth the City of Bethany * seated upon a foal, * thereby
                destroying the most wicked and barren folly of old, ** of the Gentiles.
                Now & Ever ..., in Tone II:
                Today Christ entereth the City of Bethany * seated upon a foal, * thereby
                destroying the most wicked and barren folly of old, ** of the Gentiles.
                In Tone VI: Have mercy on me, O God, * according to Thy great mercy; *
                and according to the multitude of Thy compassions, ** blot out my
                transgressions.
                In the same Tone: Today the grace of the Holy Spirit * hath gathered us
                together, * and having taken up Thy Cross, we all say: * “Blessed is He that
                cometh in the Name of the Lord; ** Hosanna in the highest”.
            """
            ,'canon': """
                Canon, in Tone IV:
                ODE I:
                Irmos: The springs of the deep were seen bereft of water, * and the
                foundations of the storm-tossed sea were laid bare by the wind: * For by
                Thy command Thou didst rebuke the sea * and thereby save Thy chosen
                people, * as they sang to Thee, O Lord, a hymn of victory.
                Refrain: Glory to Thee our God, glory to Thee.
                Out of the mouth of babes and sucklings hast thou perfected praise, Thou
                hast overthrown the adversary and by Thy Passion on the Cross avenged Adam’s
                ancient fall; with the Tree Thou hast raised him up, wherefore he singeth unto
                Thee a hymn of victory O Lord.
                Glory ..., Now & Ever ..., The Church of the venerable saints offereth Thee
                praise, O Christ, Thou Who dwellest in Zion, and Israel rejoiceth in Thee that
                made her. The mountains, prefiguring the stony-hearted Gentiles, exult
                exceedingly before Thy countenance, and they sing unto Thee a hymn of victory,
                O Lord.
                Katavasia in Tone IV: The springs of the deep were seen bereft of water, *
                and the foundations of the storm-tossed sea were laid bare by the wind: *
                For by Thy command Thou didst rebuke the sea * and thereby save Thy
                chosen people, * as they sang to Thee, O Lord, a hymn of victory.
                ODE III
                Irmos: The people of Israel drew water from a solid rock, * for at Thy
                command it became a flowing stream. * O Christ, Who art Thyself our
                rock and our life; * on Thee hath the Church been founded, * and to Thee
                doth she cry aloud: * Hosanna, blessed is He that cometh.
                Refrain: Glory to Thee our God, glory to Thee.
                Trembling at Thy command, Hades yielded up Lazarus who was four days
                dead. For Thou, O Christ, art the resurrection and the life; on Thee the Church
                is founded, and she crieth aloud: “Hosanna, blessed art Thou that hast come”.
                Glory ..., Now & Ever ..., O ye people, sing in Zion a hymn fitting for God,
                and offer prayer to Christ in Jerusalem. For He cometh in power and glory: On
                Him the Church is founded, and she crieth aloud: “Hosanna, blessed art Thou
                that hast come”.
                Katavasia: The people of Israel drew water from a solid rock, * for at Thy
                command it became a flowing stream. * O Christ, Who art Thyself our
                rock and our life; * on Thee hath the Church been founded, * and to Thee
                doth she cry aloud: * Hosanna, blessed is He that cometh.
                Sessional Hymn, in Tone VI:
                Those who sang in praise of Christ God with branches, * seized Him and
                crucified Him on the Cross, O ye ungrateful Jews! * But we with never-changing
                faith ever honor Him as the Benefactor, ever hymning Him: ** “Blessed art
                Thou that comest to call back Adam.
                ODE IV
                Irmos: “Christ cometh, manifestly revealing Himself as our God; * He
                shall come and not tarry, * from the thickly wooded mountain, * born of a
                Maiden who hath not known a man.” * thus did the Prophet say of old, *
                wherefore we cry aloud: * “Glory to Thy power, O Lord”.
                Refrain: Glory to Thee our God, glory to Thee.
                Let the strong and revered mountains and hills burst forth with rejoicing,
                and let the trees of the forest clap their hands. Give ye praise unto Christ, all ye
                nations, and magnify Him all ye peoples, crying aloud: “Glory to Thy power, O
                Lord”.
                Glory ...: The Lord, the King of the ages, cometh clothed in strength and
                glory, and splendorous is His beauty in Zion. Wherefore we all cry aloud: “Glory
                to Thy power, O Lord”.
                Now & Ever ..., The Lord hath come, He Who measures the heavens, and
                in Whose hand the earth is held. For He hath chosen Zion, and there hath He
                been pleased to dwell and rule, and to love His people who cry aloud with faith:
                “Glory to Thy power, O Lord”.
                Katavasia: “Christ cometh, manifestly revealing Himself as our God; * He
                shall come and not tarry, * from the thickly wooded mountain, * born of a
                Maiden who hath not known a man.” * thus did the Prophet say of old, *
                wherefore we cry aloud: * “Glory to Thy power, O Lord”.
                ODE V
                Irmos: Ascend the mountain, Thou that bringest good tidings unto Zion;
                * and Thou that preachest to Jerusalem, * with strength lift up Thy voice.
                * Glorious things are spoken of thee, O City of God: * Peace be upon
                Israel and salvation unto the Gentiles.
                Refrain: Glory to Thee our God, glory to Thee.
                God Who is seated on high upon the cherubim and yet careth for the
                humble, has Himself come in power and glory, wherefore all things are filled
                with His divine praise. Peace be upon Israel and salvation unto the Gentiles.
                Glory ..., Now & Ever ..., O Zion, thou holy mountain of God, and
                Jerusalem, lift up thine eyes round about thee and behold thy children, gathered
                in thee. For lo, they have come from afar to worship thy King. Peace be upon
                Israel and salvation unto the Gentiles.
                Katavasia: Ascend the mountain, Thou that bringest good tidings unto
                Zion; * and Thou that preachest to Jerusalem, * with strength lift up Thy
                voice. * Glorious things are spoken of thee, O City of God: * Peace be
                upon Israel and salvation unto the Gentiles.
                ODE VI
                Irmos: The spirits of the righteous cried aloud in joy: * “Now hath a new
                covenant been granted unto the world: * Let the people therein be
                renewed * by the sprinkling of the Blood of God.”
                Refrain: Glory to Thee our God, glory to Thee.
                O Israel, receive thou God’s Kingdom, and let him that walketh in darkness
                see the great light, and let the people be renewed by the sprinkling of the Blood
                of God.
                Glory ..., Now & Ever ..., Set free thy prisoners, O Zion, and let them go;
                bring them out of the waterless pit of ignorance; and let the people be renewed
                by sprinkling with the Blood of God.
                Katavasia: The spirits of the righteous cried aloud in joy: * “Now hath a
                new covenant been granted unto the world: * Let the people therein be
                renewed * by the sprinkling of the Blood of God.”
                Kontakion, in Tone VI:
                Being borne upon a throne in heaven, and upon a colt on the earth, * O
                Christ God, Thou didst accept the praise of the angels * and the laudation of the
                children as they cry to Thee: ** Blessed is He that cometh to recall Adam.
                Ikos: O immortal One, Thou didst bound Hades, and slay death, and raise
                up the world: therefore the children, carrying palms, and singing praises unto
                Thee as Victor, O Christ, cried aloud to Thee this day: “Hosanna to the Son of
                David! For no more,” said they, “shall children be slain because of the Child of
                Mary; for Thou alone art crucified for all, both young and old. No more shall the
                sword be drawn against us, for Thy side hath been pierced by a spear”.
                Wherefore with great rejoicing, we cry aloud: “Blessed art Thou Who hast come
                to call back Adam.”
                SYNAXARION READING
                Verse: He Who openeth the heavens is seated upon a colt;
                Verse: Seeking out mankind ...
                On this day, Palm Sunday, we celebrate the bright and glorious feast of the
                Entrance of our Lord Jesus Christ into Jerusalem. After the raising of Lazarus
                from the dead, many people who witnessed this event believed in Christ.
                Moreover, a decree was passed by the council of the Jews to have both Christ
                and Lazarus killed. Therefore, giving place to their wickedness, Jesus withdrew.
                The Jews, for their part, made plans to kill Him during the Feast of the Passover.
                Having stayed away for a long time in the wilderness near Ephraim, six days
                before the Passover Jesus came to Bethany to the house of Lazarus, who had
                been dead. There at supper, Lazarus ate with Him, and his sister Mary poured
                ointment on Christ’s feet. Since Lazarus had been raised from the dead,
                numerous Jews had forsaken the lifeless synagogue and believed in Jesus. In the
                future, these would be recognized as the first Christians. At this time, the Jews
                were divided between those who wished Christ dead and were planning His
                death and those who acknowledged Him as the Messiah. The next day, Jesus sent
                his Disciples to bring an ass and a colt. And He, who has heaven as a throne,
                entered Jerusalem seated on a colt. Meanwhile, the children of the Jews spread
                their garments and branches of trees on the road before Him. Others cut
                branches and others held them in their hands, going before Him shouting,
                “Hosanna to the Son of David! Blessed is He who comes in the name of the
                Lord, the King of Israel!” (John 12:13). This took place because the Most holy
                Spirit moved their tongues in praise and exaltation of Christ. By using palms (in
                Hebrew, the tender branch is called “vaion”, a palm branch), they were signifying
                Christ’s imminent victory over death. For it was the custom to honor the victors
                of contests or battles with triumphal processions and to lead them around with
                branches from evergreens. The meaning of Hosanna is “save now, we pray” or
                “Therefore, save.” The colt prefigured us, the Gentiles. The ass’s colt was still an
                untamed animal and impure according to the Jewish law. Christ’s sitting and
                resting on the “Gentiles” showed our taming and obedience to the “law” of the
                Holy Gospel and Christ as Champion, Victor, and King of all the earth. Today
                we not only welcome the Lord riding on a colt into the city of Jerusalem, but
                Christ who comes in power and glory as King of the age to come. Yet this King
                comes in meekness and, humility, much different from the triumphal entry of
                earthly| rulers. The multitudes beheld a man riding an ass’s colt into the earthly
                city of Jerusalem to be proclaimed “King of the Jews” the Liberator from the
                Roman yoke. The Church sees the Son of God, the Prince of Peace, entering the
                heavenly Jerusalem to establish His eternal reign, after His self-emptying
                Crucifixion and soul-saving Resurrection. The Prophet Zechariah was speaking
                about this feast when he said, “Fear not, О daughter of Zion; behold, your King
                is coming, sitting on an ass’s colt” (Zech. 9:9). And the Holy Prophet David
                spoke about the children, saying, “Out of the mouths of babes and sucklings.
                You have perfected praise” (Ps. 8:2). When Christ entered Jerusalem, all the city
                was in an uproar. In retaliation, the wicked Jewish High Priests instigated the
                crowds to kill Him. But Jesus evaded them, both hiding and then appearing,
                speaking to them in parables.
                By Thine ineffable compassion, О Christ our God, make us
                victorious over the irrational passions, and deem us worthy to
                see Thy manifest victory over death and Thy joyous and Life-bearing
                Resurrection, and have mercy on us and save us.
                Amen.
                ODE VII
                Irmos: Thou didst save the children of Abraham in the fire * and slay the
                Chaldeans, * who unjustly entrapped the righteous ones. * O God of our
                fathers, * supremely praised, and blessed art Thou O Lord.
                Refrain: Glory to Thee our God, glory to Thee.
                With palms in their hands, the people worshiped and rejoiced with the
                disciples, saying: “Hosanna to the Son of David” and crying: “O Lord God of
                the fathers, supremely praised, and blessed art Thou”.
                Glory ..., The multitudes of innocent ones, still yet children, hymned Thee,
                the King of Israel and of the angels, in Godly manner singing: “O Lord God of
                the fathers, supremely praised, and blessed art Thou”.
                Now & Ever ..., With palms and branches the multitudes greeted Thee, O
                Christ, praising Thee: “Blessed is He that cometh, the King of the ages”, and
                crying “O Lord God of the fathers, supremely praised, and blessed art Thou”.
                Katavasia: Thou didst save the children of Abraham in the fire * and slay
                the Chaldeans, * who unjustly entrapped the righteous ones. * O God of
                our fathers, * supremely praised, and blessed art Thou O Lord.
                ODE VIII
                Irmos: Rejoice, O Jerusalem, * and ye that love Zion, be ye festive. * For
                the Lord of Hosts Who ruleth unto all ages hath come. * Let all the earth
                stand in reverence before His countenance and cry aloud: * Bless the
                Lord, all ye works of the Lord!”.
                Refrain: Glory to Thee our God, glory to Thee.
                Riding upon a young foal, Christ thy King is at hand, O Zion. For He hath
                come to destroy the senseless delusion of idolatry and to restrain the untamed
                will of the Gentiles, so that they may sing: “O all ye works of the Lord, bless ye
                the Lord”.
                Refrain: Let us bless the Father, Son, and Holy Spirit, the Lord!
                Greatly rejoice, O Zion, for Christ thy God shall reign throughout the ages.
                As it is written, He is meek and bringeth salvation. Our righteous Redeemer hath
                come riding on a foal, that He may slay the proud arrogance of His enemies who
                cannot cry: “O all ye works of the Lord, bless ye the Lord”.
                Now & Ever ..., The lawless company of disobedient men hath been driven
                out from the temple, for they made of God’s house of prayer, a den of thieves,
                and in their hearts rejected the Redeemer, unto Whom we cry aloud: “O all ye
                works of the Lord, bless ye the Lord”.
                Sticheron: We praise, bless and worship the Lord, chanting and
                supremely exalting Him throughout all ages.
                Katavasia: Rejoice, O Jerusalem, * and ye that love Zion, be ye festive. *
                For the Lord of Hosts Who ruleth unto all ages hath come. * Let all the
                earth stand in reverence before His countenance and cry aloud: * Bless
                the Lord, all ye works of the Lord!”.
                (There is no Magnificat, ODE IX is straightway chanted)
                ODE IX
                Irmos: The Lord is God and hath appeared unto us; * let us come together
                and keep the feast with great rejoicing * let us magnify Christ with palms
                and branches, * and let us cry aloud: * Blessed is He that cometh in the
                Name of the Lord our Savior.
                Refrain: Glory to Thee our God, glory to Thee.
                Why do ye rage, O ye heathen? and Ye scribes and priests, why do ye
                imagine vain things, saying: “Who is this to Whom the children cry aloud with
                palms and branches, singing: “Blessed is He that cometh in the Name of the
                Lord our Savior?”
                Glory ..., This is our God, and there is none other like Him; He hath found
                out every righteous path, and hath given them to Israel His beloved; after which
                He manifest Himself upon the earth and lived among mankind. “Blessed is He
                that cometh in the Name of the Lord our Savior”.
                Now & Ever ..., O disobedient nation, why do ye set stumbling-blocks upon
                our path? Your feet are swift to shed the blood of the Master, but He shall rise
                again, to save all those who cry: “Blessed is He that cometh in the Name of the
                Lord our Savior”.
                Katavasia: The Lord is God and hath appeared to us; * let us keep the
                feast together. * Come, and with great rejoicing * let us magnify Christ
                with palms and branches, * and let us cry aloud: * Blessed is He that
                cometh in the Name of the Lord our Savior.
            """
            ,'praises':"""
                in Tone IV:
                Verse: To do among them the judgment that is written. This glory shall
                be to all His saints.
                A multitude of peoples spread their garments in the way, O Lord; * others
                cut down branches from the trees and carried them. * Walking before and after
                Thee, they cried aloud: * “Hosanna to the Son of David: * Blessed art Thou Who
                hast come and Who shalt come again ** in the Name of the Lord.”
                Verse: Praise ye God in His saints, * praise Him in the firmament of
                His power.
                Repeat: A multitude of peoples spread their garments ...,
                Verse: Praise Him for His mighty acts, praise Him according to the
                multitude of His greatness.
                When it was Thy will to enter the Holy City, O Lord, * the people carried
                branches from the trees and hymned Thee, the Master of all. * They saw Thee
                seated on a foal as though upon the cherubim, * wherefore they cried aloud: *
                “Blessed art Thou Who hast come ** and Who shalt come again in the Name of
                the Lord.”
                Verse: Praise Him with the sound of trumpet, * praise Him with
                psaltery and harp.
                Repeat: When it was Thy will to enter the Holy City ...,
                Verse: Praise Him with timbrel and dance, * praise Him with strings
                and flute.
                Come forth, O ye nations, * and come forth, O ye peoples: * Look ye today
                upon the King of heaven, * Who entereth Jerusalem seated upon a humble colt *
                as though upon a lofty throne. * O ye unbelieving and adulterous generation of
                Jews, * draw ye near and look upon Him * Whom once Isaiah saw coming in the
                flesh for our sakes. * Come see ye how He weds the chaste New Zion, * and
                rejecteth the condemned synagogue. * As at an incorrupt undefiled marriage, *
                the pure and innocent children gather to sing praises. * Let us also with them
                sing the hymn of the angels: * “Hosanna in the highest ** unto Him to Whom
                belongeth great mercy”.
                Verse: Praise Him with tuneful cymbals, praise Him with cymbals of
                jubilation. * Let every breath praise the Lord.
                Before Thy voluntary Passion, O Christ God, * Thou didst confirm the
                general resurrection; * for at Bethany Thou didst raise by Thine almighty power *
                Lazarus who was four days dead, * and as the Giver of Light, O Savior, * Thou
                hast made the blind to see. * With Thy disciples Thou didst enter the Holy City,
                * seated upon the foal of an ass as if upon the cherubim, * and thus didst Thou
                fulfill the preaching of the prophets. * The children of the Hebrews with palms
                and branches came to meet Thee. * Therefore we also, bearing palms and olive
                branches, cry aloud in thanksgiving unto Thee: ** “Hosanna in the highest;
                blessed is He that cometh in the Name of the Lord”.
                Glory ..., Now & Ever ..., in Tone VI:
                Six days before the Passover Jesus entered Bethany, * and His disciples
                came up to Him, saying unto Him: * “O Lord, where wilt Thou that we prepare
                for Thee to eat the Passover?” * He then sent them, saying: * “Go ye into the
                village opposite, * and there ye shall find a man bearing a pitcher of water; *
                follow him, and tell the master of the house: * The Teacher hath said, In thy
                house shall I eat the Passover ** with My disciples.”
            """
            ,'apolytichia':"""
                in Tone I:
                In confirming the common Resurrection, O Christ God, * Thou
                didst raise up Lazarus from the dead before Thy passion. * Wherefore, we also,
                like the children bearing the symbols of victory, * cry to Thee, the Vanquisher of
                death: * Hosanna in the highest; ** blessed is He that cometh in the name of the
                Lord.
            """
        } #Matins
        ,'liturgy': {
            'festal_antiphon1':"""
                The First Antiphon in Tone II:
                Verse: I am filled with love, * for the Lord will hear the voice of my
                supplication.
                Refrain: Through the prayers of the Theotokos, O Savior, save us.
                Verse: For He hath inclined His ear unto me, * and in my days will I
                call upon Him.
                Refrain: Through the prayers of the Theotokos, O Savior, save us.
                Verse: The pangs of death have encompassed me, * the perils of Hades
                have found me.
                Refrain: Through the prayers of the Theotokos, O Savior, save us.
                Verse: Tribulation and sorrow have I found, * and I called upon the
                name of the Lord.
                Refrain: Through the prayers of the Theotokos, O Savior, save us.
                Glory ..., Now & Ever ...,
                Refrain: Through the prayers of the Theotokos, O Savior, save us.
            """
            ,'festal_antiphon2':"""
                The Second Antiphon in Tone II:
                Verse: I believed, wherefore I spake; * I was humbled exceedingly.
                Refrain: O Son of God Who didst sit upon a colt, save us who sing to
                Thee: Alleluia.
                Verse: What shall I render unto the Lord * for all that He hath
                rendered unto me?
                Refrain: O Son of God Who didst sit upon a colt, save us who sing to
                Thee: Alleluia.
                Verse: I will take the cup of salvation, * and I will call upon the name of
                the Lord.
                Refrain: O Son of God Who didst sit upon a colt, save us who sing to
                Thee: Alleluia.
                Verse: My vows unto the Lord will I pay * in the presence of all His
                people.
                Refrain: O Son of God Who didst sit upon a colt, save us who sing to
                Thee: Alleluia.
                Glory ..., Now & Ever ...,
                O only-begotten Son and Word of God, * Who art immortal, * yet didst
                deign for our salvation to be incarnate of the Holy Theotokos and Ever-Virgin
                Mary, * and without change didst become man, * and was crucified, O Christ
                God, trampling down death by death. * Thou Who art one of the Holy Trinity,
                ** glorified with the Father and the Holy Spirit, save us.
            """
            ,'festal_antiphon3':"""
                The Third Antiphon:
                Verse: O give thanks unto the Lord, for He is good, for His mercy
                endureth forever.
                Troparion of the Feast: in Tone I:
                In confirming the common Resurrection, O Christ God, * Thou
                didst raise up Lazarus from the dead before Thy passion. * Wherefore, we also,
                like the children bearing the symbols of victory, * cry to Thee, the Vanquisher of
                death: * Hosanna in the highest; ** blessed is He that cometh in the name of the
                Lord.
                Verse: Let the house of Israel now say that He is good, for His mercy
                endureth forever.
                Choir, Repeat: In confirming the common Resurrection ...,
                Verse: Let the house of Aaron now say that He is good, for His mercy
                endureth forever.
                Choir, Repeat: In confirming the common Resurrection ...,
                Verse: Let all that fear the Lord now say that He is good, for His mercy
                endureth forever.
                Choir, Repeat: In confirming the common Resurrection ...,
                The entry verse (Introit): Blessed is he that cometh in the name of the
                Lord. We have blessed you out of the house of the Lord. God is the
                Lord, and hath appeared unto us.
            """
            ,'troparion':"""
                Tone I: In confirming the common Resurrection, O Christ God, * Thou
                didst raise up Lazarus from the dead before Thy passion. * Wherefore, we also,
                like the children bearing the symbols of victory, * cry to Thee, the Vanquisher of
                death: * Hosanna in the highest; ** blessed is He that cometh in the name of the
                Lord.
                Glory..., in Tone IV: As by baptism we were buried with Thee, O Christ our
                God, * so by Thy Resurrection we were deemed worthy of immortal life; *
                and praising Thee, we cry: * Hosanna in the highest; ** blessed is He that
                cometh in the name of the Lord.
            """
            ,'kontakion': """
                Both now..., in Tone VI: Being borne upon a throne in heaven, and upon a
                colt on the earth, * O Christ God, Thou didst accept the praise of the angels *
                and the laudation of the children as they cry to Thee: ** Blessed is He that
                cometh to recall Adam.
            """
            ,'prokeimenon':"""
                Prokeimenon, in Tone IV: Blessed is he that cometh in the name of the
                Lord. * God is the Lord, and hath appeared unto us.
                Verse: O give thanks unto the Lord, for He is good, for His mercy
                endureth forever.
            """
            ,'readings': """
                EPISTLE TO THE PHILIPPIANS: (4:4-9)
                Brethren: Rejoice in the Lord always: and again I say, Rejoice. Let your
                moderation be known unto all men. The Lord is at hand. Be careful for nothing;
                but in every thing by prayer and supplication with thanksgiving let your requests
                be made known unto God. And the peace of God, which passeth all
                understanding, shall keep your hearts and minds through Christ Jesus. Finally,
                brethren, whatsoever things are true, whatsoever things are honest, whatsoever
                things are just, whatsoever things are pure, whatsoever things are lovely,
                whatsoever things are of good report; if there be any virtue, and if there be any
                praise, think on these things. Those things, which ye have both learned, and
                received, and heard, and seen in me, do: and the God of peace shall be with you
                Alleluia in Tone I: O sing unto the Lord a new song, for the Lord hath
                wrought wondrous things.
                Verse: All the ends of the earth have seen the salvation of our God.
                GOSPEL ACCORDING TO ST. JOHN (12:1-18)
                Six days before the Passover Jesus came to Bethany, where Lazarus was,
                which had been dead, whom he raised from the dead. There they made him a
                supper; and Martha served: but Lazarus was one of them that sat at the table
                with him. Then took Mary a pound of ointment of spikenard, very costly, and
                anointed the feet of Jesus, and wiped his feet with her hair: and the house was
                filled with the odor of the ointment. Then saith one of his disciples, Judas
                Iscariot, Simon’s son, which should betray him, Why was not this ointment sold
                for three hundred pence, and given to the poor? This he said, not that he cared
                for the poor; but because he was a thief, and had the bag, and bare what was put
                therein. Then said Jesus, Let her alone: against the day of my burying hath she
                kept this. For the poor always ye have with you; but me ye have not always.
                Much people of the Jews therefore knew that he was there: and they came not
                for Jesus’ sake only, but that they might see Lazarus also, whom he had raised
                from the dead. But the chief priests consulted that they might put Lazarus also to
                death; Because that by reason of him many of the Jews went away, and believed
                on Jesus. On the next day much people that were come to the feast, when they
                heard that Jesus was coming to Jerusalem, Took branches of palm trees, and
                went forth to meet him, and cried, Hosanna: Blessed is the King of Israel that
                cometh in the name of the Lord. And Jesus, when he had found a young ass, sat
                thereon; as it is written, Fear not, daughter of Zion: behold, thy King cometh,
                sitting on an ass’s colt. These things understood not his disciples at the first: but
                when Jesus was glorified, then remembered they that these things were written of
                him, and that they had done these things unto him. The people therefore that
                was with him when he called Lazarus out of his grave, and raised him from the
                dead, bare record. For this cause the people also met him, for that they heard
                that he had done this miracle.
                Instead of “It is truly meet…” we chant the Irmos of the 9th ODE of the
                First Canon of the feast, Tone IV:
                Irmos: The Lord is God and hath appeared to us; * let us keep the feast
                together. * Come, and with great rejoicing * let us magnify Christ with
                palms and branches, * and let us cry aloud: * Blessed is He that cometh in
                the Name of the Lord our Savior.
            """
        } #Liturgy
    } #Service


#5th Thurs, Canon of St Andrew  -17
#5th Sat, Akathist              -15
#5th | Sunday of St martyrs     -14
#6th Sat Lazarus Saturdays      -8
#   Palm Sunday                 -7
#   Holy Monday                 -6
#   Holy Tuesday                -5
#   Holy Wednesday              -4
#   Holy Thursday               -3
#   Holy Friday                 -2
#   Holy Saturdays              -1
#   Pascha                      0

} #end of Triodion Dictionary

with open('test.html', 'w') as f:
    readings = '<p>' + triodion.get('-35').get('vespers').get('aposticha_theotokion') + '</p>'
    print (format_text(readings))
    f.write(format_text(readings))

template = {
    'test': 'test'
    ,'offset': {
        'vespers': {
            'stichera_tone': ''
            ,'stichera': [
                """

                """
                ,"""

                """
                ,"""

                """
                ,"""

                """
            ]
            ,'doxastichon': """

            """
            ,'aposticha_theotokion': """

            """
        } #Vespers
        ,'matins': {
            'troparion': """

            """
            ,'evlogitaria':"""

            """
            ,'after50': """

            """
            ,'canon': """

            """
            ,'exapostilarion': """

            """
            ,'praises':"""

            """
            ,'aposticha': """

            """
            ,'aposticha_theotokion': """

            """
            ,'apolytichia':"""

            """
        } #Matins
        ,'liturgy': {
            'beatitudes': [
                """

                """
                ,"""

                """
                ,"""

                """
                ,"""

                """
            ]
            ,'troparion':"""

            """
            ,'kontakion': """

            """
            ,'prokeimenon':"""

            """
            ,'readings': """

            """
        } #Liturgy
    } #Service
}
