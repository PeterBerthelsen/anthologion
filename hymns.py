"""
Version 0.1.3
Updated 10/21/2021

Change Log:
10/13/2021 - 0.1.0 - Initial Working Build - vespers prokeimena added
10/21/2021 - 0.1.3 - Update file name, incorporated with jinja templates
"""
daily_vespers_prokeimena = {
    0: '<p class="note">In the Eighth Tone:</p><p>Behold now, bless ye the Lord, all ye servants of the Lord.</p><p><i class="note">Stichos:</i> Ye that stand in the house of the Lord, in the courts of the house of our God.</p>'
    ,1: '<p class="note">In the Fourth Tone:</p><p>The Lord will hearken unto me when I cry unto Him.</p><p><i class="note">Stichos:</i> When I called upon Thee, O God of my righteousness, Thou didst hearken unto me.</p>'
    ,2: '<p class="note">In the First Tone:</p><p>Thy mercy, O Lord, shall pursue me all the days of my life.</p><p><i class="note">Stichos:</i> The Lord is my shepherd, and I shall not want.  In a place of green pasture, there hath He made me to dwell.</p>'
    ,3: '<p class="note">In the Fifth Tone:</p><p>O God, in Thy name save me, and in Thy strength do Thou judge me.</p><p><i class="note">Stichos:</i> O God, hearken unto my prayer, give ear unto the words of my mouth.</p>'
    ,4: '<p class="note">In the Sixth Tone:</p><p>My help cometh from the Lord, Who hath made heaven and the earth.</p><p><i class="note">Stichos:</i> I have lifted up mine eyes to the Mountains, from whence cometh my help.</p>'
    ,5: '<p class="note">In the Seventh Tone:</p><p>O God, my helper art Thou, and Thy mercy shall go before me.</p><p><i class="note">Stichos:</i> Rescue me from mine enemies, O God, and from them that rise up against me redeem me.</p>'
    ,6: '<p class="note">In the Sixth Tone:</p><p>The Lord is King, He is clothed with majesty.</p><p><i class="note">Stichos 1:</i> The Lord is clothed with strength and He hath girt Himself.</p><p><i class="note">Stichos 2:</i> For He established the world which shall not be shaken.</p><p><i class="note">Stichos 3:</i> Holiness becometh Thy house, O Lord, unto length of days.</p>'
}

daily_compline_troparia = {
    0: """<p>The memory of the righteous is celebrated with hymns of praise, but the Lord''s testimony is sufficient for thee, O Forerunner; for thou hast proved to be even more venerable than the prophets since thou wast granted to baptize in the running waters Him Whom they proclaimed. Wherefore, having contested for the truth, thou didst rejoice to announce the good tidings even to those in Hades; that God hath appeared in the flesh, taking away the sin of the world and granting us great mercy.</p>"""
    ,6: '<p>Supreme Commanders of the Heavenly Hosts, we unworthy ones implore you that by your supplications ye will encircle us with the shelter of the wings of your immaterial glory, and guard us who fall down before you and fervently cry: Deliver us from dangers since ye are the Marshals of the Hosts on high.</p>'
    ,1: '<p>Save, O Lord, Thy people, and bless Thine inheritance; grant Thou unto Orthodox Christians victory over enemies; and by the power of Thy Cross do Thou preserve Thy commonwealth.·</p>'
    ,2: """<p>O holy Apostles, intercede with the merciful God, that He grant unto our souls forgiveness of offenses.</p>
    <p>And to St. Nicholas, Fourth Tone:</p>
    <p>The truth of things hath revealed thee to thy flock as a rule of faith, an icon of meekness and a teacher of temperance; therefore thou hast achieved the heights by humility, riches by poverty. O Father and Hierarch Nicholas, intercede with Christ God that our souls be saved.</p>"""
    ,3: '<p>Save, O Lord, Thy people, and bless Thine inheritance; grant Thou unto Orthodox Christians victory over enemies; and by the power of Thy Cross do Thou preserve Thy commonwealth.</p>'
    ,4: """<p>O Apostles, Martyrs, and Prophets, Venerable and Righteous Ones; ye that have accomplished a good labor and kept the Faith, that have boldness before the Savior; O Good Ones, intercede for us, we pray, that our souls be saved.</p>
    <p>Glory to the Father and to the Son, and to the Holy Spirit.</p>
    <p>With the saints give rest, O Christ, to the souls of Thy servants, where there is neither sickness, nor sorrow, nor sighing, but life everlasting.</p>
    <p>Both now and ever, and unto the ages of ages. Amen.</p>
    <p>To Thee, O Lord, the Planter of creation, the world doth offer the God-bearing martyrs as the first-fruits of nature. By their intercessions preserve Thy Church, Thy commonwealth, in profound peace, through the Theotokos, O Greatly-merciful One.</p>"""
}

def vespers_prokeimena(weekday:int):
    return daily_vespers_prokeimena.get(weekday)

def compline_troparia(weekday:int, rank:int=7):
    payload = daily_compline_troparia.get(weekday, '')
    if rank == 7 and (5 < weekday < 4):
        payload +='<p>O God of our fathers, Who ever dealest with us according to Thy kindness, do not withdraw Thy mercy from us, but through their intercessions guide our life in peace.</p>'
        payload +='<p>Adorned in the blood of Thy martyrs throughout all the world, as in purple and fine linen, Thy Church, through them, doth cry unto Thee, O Christ God: Send down Thy compassions upon Thy people; grant to Thy community, and to our souls great mercy.</p>'
        payload +='<p>Glory to the Father, and to the Son, and to the Holy Spirit.</p>'
        payload +='<p>With the saints give rest, O Christ, to the souls of Thy servants, where there is neither sickness, nor sorrow, nor sighing, but life everlasting.</p>'
        payload +='<p>Both now and ever, and unto the ages of ages. Amen.</p>'
        payload += '<p>Through the intercessions, O Lord, of all the saints and the Theotokos, grant us Thy peace, and have mercy on us, as Thou alone art compassionate.</p>'
    return payload
