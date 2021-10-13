"""
Version 0.1.0
Updated 10/13/2021

Change Log:
10/13/2021 - 0.1.0 - Initial Working Build - vespers prokeimena added
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

def vespers_prokeimena(weekday:int):
    return daily_vespers_prokeimena.get(weekday)
