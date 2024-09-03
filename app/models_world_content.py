CSRF_COOKIE_SECURE: False
SESSION_COOKIE_SECURE: False
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ItemTemplates(models.Model):
    name = models.CharField(max_length=86)
    icon = models.CharField(max_length=256, blank=True, null=True)
    icon2 = models.TextField()
    category = models.CharField(max_length=86, blank=True, null=True)
    subcategory = models.CharField(max_length=86, blank=True, null=True)
    itemtype = models.CharField(db_column='itemType', max_length=86, blank=True, null=True)  # Field name made lowercase.
    subtype = models.CharField(db_column='subType', max_length=86, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(max_length=86, blank=True, null=True)
    display = models.CharField(max_length=128, blank=True, null=True)
    slot1 = models.CharField(max_length=86)
    drawweaponeffect1 = models.TextField(db_column='drawWeaponEffect1')  # Field name made lowercase.
    drawweapontime1 = models.IntegerField(db_column='drawWeaponTime1')  # Field name made lowercase.
    holsteringweaponeffect1 = models.TextField(db_column='holsteringWeaponEffect1')  # Field name made lowercase.
    holsteringweapontime1 = models.IntegerField(db_column='holsteringWeaponTime1')  # Field name made lowercase.
    slot2 = models.CharField(max_length=86)
    drawweaponeffect2 = models.TextField(db_column='drawWeaponEffect2')  # Field name made lowercase.
    drawweapontime2 = models.IntegerField(db_column='drawWeaponTime2')  # Field name made lowercase.
    holsteringweaponeffect2 = models.TextField(db_column='holsteringWeaponEffect2')  # Field name made lowercase.
    holsteringweapontime2 = models.IntegerField(db_column='holsteringWeaponTime2')  # Field name made lowercase.
    slot3 = models.CharField(max_length=86)
    drawweaponeffect3 = models.TextField(db_column='drawWeaponEffect3')  # Field name made lowercase.
    drawweapontime3 = models.IntegerField(db_column='drawWeaponTime3')  # Field name made lowercase.
    holsteringweaponeffect3 = models.TextField(db_column='holsteringWeaponEffect3')  # Field name made lowercase.
    holsteringweapontime3 = models.IntegerField(db_column='holsteringWeaponTime3')  # Field name made lowercase.
    slot4 = models.CharField(max_length=86)
    drawweaponeffect4 = models.TextField(db_column='drawWeaponEffect4')  # Field name made lowercase.
    drawweapontime4 = models.IntegerField(db_column='drawWeaponTime4')  # Field name made lowercase.
    holsteringweaponeffect4 = models.TextField(db_column='holsteringWeaponEffect4')  # Field name made lowercase.
    holsteringweapontime4 = models.IntegerField(db_column='holsteringWeaponTime4')  # Field name made lowercase.
    slot5 = models.CharField(max_length=86)
    drawweaponeffect5 = models.TextField(db_column='drawWeaponEffect5')  # Field name made lowercase.
    drawweapontime5 = models.IntegerField(db_column='drawWeaponTime5')  # Field name made lowercase.
    holsteringweaponeffect5 = models.TextField(db_column='holsteringWeaponEffect5')  # Field name made lowercase.
    holsteringweapontime5 = models.IntegerField(db_column='holsteringWeaponTime5')  # Field name made lowercase.
    slot6 = models.CharField(max_length=86)
    drawweaponeffect6 = models.TextField(db_column='drawWeaponEffect6')  # Field name made lowercase.
    drawweapontime6 = models.IntegerField(db_column='drawWeaponTime6')  # Field name made lowercase.
    holsteringweaponeffect6 = models.TextField(db_column='holsteringWeaponEffect6')  # Field name made lowercase.
    holsteringweapontime6 = models.IntegerField(db_column='holsteringWeaponTime6')  # Field name made lowercase.
    slot7 = models.CharField(max_length=86)
    drawweaponeffect7 = models.TextField(db_column='drawWeaponEffect7')  # Field name made lowercase.
    drawweapontime7 = models.IntegerField(db_column='drawWeaponTime7')  # Field name made lowercase.
    holsteringweaponeffect7 = models.TextField(db_column='holsteringWeaponEffect7')  # Field name made lowercase.
    holsteringweapontime7 = models.IntegerField(db_column='holsteringWeaponTime7')  # Field name made lowercase.
    slot8 = models.CharField(max_length=86)
    drawweaponeffect8 = models.TextField(db_column='drawWeaponEffect8')  # Field name made lowercase.
    drawweapontime8 = models.IntegerField(db_column='drawWeaponTime8')  # Field name made lowercase.
    holsteringweaponeffect8 = models.TextField(db_column='holsteringWeaponEffect8')  # Field name made lowercase.
    holsteringweapontime8 = models.IntegerField(db_column='holsteringWeaponTime8')  # Field name made lowercase.
    slot9 = models.CharField(max_length=86)
    drawweaponeffect9 = models.TextField(db_column='drawWeaponEffect9')  # Field name made lowercase.
    drawweapontime9 = models.IntegerField(db_column='drawWeaponTime9')  # Field name made lowercase.
    holsteringweaponeffect9 = models.TextField(db_column='holsteringWeaponEffect9')  # Field name made lowercase.
    holsteringweapontime9 = models.IntegerField(db_column='holsteringWeaponTime9')  # Field name made lowercase.
    slot10 = models.CharField(max_length=86)
    drawweaponeffect10 = models.TextField(db_column='drawWeaponEffect10')  # Field name made lowercase.
    drawweapontime10 = models.IntegerField(db_column='drawWeaponTime10')  # Field name made lowercase.
    holsteringweaponeffect10 = models.TextField(db_column='holsteringWeaponEffect10')  # Field name made lowercase.
    holsteringweapontime10 = models.IntegerField(db_column='holsteringWeaponTime10')  # Field name made lowercase.
    itemquality = models.IntegerField(db_column='itemQuality', blank=True, null=True)  # Field name made lowercase.
    binding = models.IntegerField(blank=True, null=True)
    isunique = models.IntegerField(db_column='isUnique', blank=True, null=True)  # Field name made lowercase.
    stacklimit = models.IntegerField(db_column='stackLimit', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(blank=True, null=True)
    purchasecurrency = models.IntegerField(db_column='purchaseCurrency', blank=True, null=True)  # Field name made lowercase.
    purchasecost = models.BigIntegerField(db_column='purchaseCost', blank=True, null=True)  # Field name made lowercase.
    sellable = models.IntegerField(blank=True, null=True)
    damage = models.IntegerField()
    damagemax = models.IntegerField(db_column='damageMax')  # Field name made lowercase.
    damagetype = models.CharField(db_column='damageType', max_length=86, blank=True, null=True)  # Field name made lowercase.
    delay = models.FloatField(blank=True, null=True)
    tooltip = models.CharField(db_column='toolTip', max_length=255, blank=True, null=True)  # Field name made lowercase.
    triggerevent = models.CharField(db_column='triggerEvent', max_length=86, blank=True, null=True)  # Field name made lowercase.
    triggeraction1type = models.CharField(db_column='triggerAction1Type', max_length=86, blank=True, null=True)  # Field name made lowercase.
    triggeraction1data = models.CharField(db_column='triggerAction1Data', max_length=86, blank=True, null=True)  # Field name made lowercase.
    effect1type = models.CharField(max_length=86, blank=True, null=True)
    effect1name = models.CharField(max_length=86, blank=True, null=True)
    effect1value = models.CharField(max_length=86, blank=True, null=True)
    effect2type = models.CharField(max_length=86, blank=True, null=True)
    effect2name = models.CharField(max_length=86, blank=True, null=True)
    effect2value = models.CharField(max_length=86, blank=True, null=True)
    effect3type = models.CharField(max_length=86, blank=True, null=True)
    effect3name = models.CharField(max_length=86, blank=True, null=True)
    effect3value = models.CharField(max_length=86, blank=True, null=True)
    effect4type = models.CharField(max_length=86, blank=True, null=True)
    effect4name = models.CharField(max_length=86, blank=True, null=True)
    effect4value = models.CharField(max_length=86, blank=True, null=True)
    effect5type = models.CharField(max_length=86, blank=True, null=True)
    effect5name = models.CharField(max_length=86, blank=True, null=True)
    effect5value = models.CharField(max_length=86, blank=True, null=True)
    effect6type = models.CharField(max_length=86, blank=True, null=True)
    effect6name = models.CharField(max_length=86, blank=True, null=True)
    effect6value = models.CharField(max_length=86, blank=True, null=True)
    effect7type = models.CharField(max_length=86, blank=True, null=True)
    effect7name = models.CharField(max_length=86, blank=True, null=True)
    effect7value = models.CharField(max_length=86, blank=True, null=True)
    effect8type = models.CharField(max_length=86, blank=True, null=True)
    effect8name = models.CharField(max_length=86, blank=True, null=True)
    effect8value = models.CharField(max_length=86, blank=True, null=True)
    effect9type = models.CharField(max_length=86, blank=True, null=True)
    effect9name = models.CharField(max_length=86, blank=True, null=True)
    effect9value = models.CharField(max_length=86, blank=True, null=True)
    effect10type = models.CharField(max_length=86, blank=True, null=True)
    effect10name = models.CharField(max_length=86, blank=True, null=True)
    effect10value = models.CharField(max_length=86, blank=True, null=True)
    effect11type = models.CharField(max_length=86, blank=True, null=True)
    effect11name = models.CharField(max_length=86, blank=True, null=True)
    effect11value = models.CharField(max_length=86, blank=True, null=True)
    effect12type = models.CharField(max_length=86, blank=True, null=True)
    effect12name = models.CharField(max_length=86, blank=True, null=True)
    effect12value = models.CharField(max_length=86, blank=True, null=True)
    effect13type = models.CharField(max_length=86, blank=True, null=True)
    effect13name = models.CharField(max_length=86, blank=True, null=True)
    effect13value = models.CharField(max_length=86, blank=True, null=True)
    effect14type = models.CharField(max_length=86, blank=True, null=True)
    effect14name = models.CharField(max_length=86, blank=True, null=True)
    effect14value = models.CharField(max_length=86, blank=True, null=True)
    effect15type = models.CharField(max_length=86, blank=True, null=True)
    effect15name = models.CharField(max_length=86, blank=True, null=True)
    effect15value = models.CharField(max_length=86, blank=True, null=True)
    effect16type = models.CharField(max_length=86, blank=True, null=True)
    effect16name = models.CharField(max_length=86, blank=True, null=True)
    effect16value = models.CharField(max_length=86, blank=True, null=True)
    effect17type = models.CharField(max_length=86, blank=True, null=True)
    effect17name = models.CharField(max_length=86, blank=True, null=True)
    effect17value = models.CharField(max_length=86, blank=True, null=True)
    effect18type = models.CharField(max_length=86, blank=True, null=True)
    effect18name = models.CharField(max_length=86, blank=True, null=True)
    effect18value = models.CharField(max_length=86, blank=True, null=True)
    effect19type = models.CharField(max_length=86, blank=True, null=True)
    effect19name = models.CharField(max_length=86, blank=True, null=True)
    effect19value = models.CharField(max_length=86, blank=True, null=True)
    effect20type = models.CharField(max_length=86, blank=True, null=True)
    effect20name = models.CharField(max_length=86, blank=True, null=True)
    effect20value = models.CharField(max_length=86, blank=True, null=True)
    effect21type = models.CharField(max_length=86, blank=True, null=True)
    effect21name = models.CharField(max_length=86, blank=True, null=True)
    effect21value = models.CharField(max_length=86, blank=True, null=True)
    effect22type = models.CharField(max_length=86, blank=True, null=True)
    effect22name = models.CharField(max_length=86, blank=True, null=True)
    effect22value = models.CharField(max_length=86, blank=True, null=True)
    effect23type = models.CharField(max_length=86, blank=True, null=True)
    effect23name = models.CharField(max_length=86, blank=True, null=True)
    effect23value = models.CharField(max_length=86, blank=True, null=True)
    effect24type = models.CharField(max_length=86, blank=True, null=True)
    effect24name = models.CharField(max_length=86, blank=True, null=True)
    effect24value = models.CharField(max_length=86, blank=True, null=True)
    effect25type = models.CharField(max_length=86, blank=True, null=True)
    effect25name = models.CharField(max_length=86, blank=True, null=True)
    effect25value = models.CharField(max_length=86, blank=True, null=True)
    effect26type = models.CharField(max_length=86, blank=True, null=True)
    effect26name = models.CharField(max_length=86, blank=True, null=True)
    effect26value = models.CharField(max_length=86, blank=True, null=True)
    effect27type = models.CharField(max_length=86, blank=True, null=True)
    effect27name = models.CharField(max_length=86, blank=True, null=True)
    effect27value = models.CharField(max_length=86, blank=True, null=True)
    effect28type = models.CharField(max_length=86, blank=True, null=True)
    effect28name = models.CharField(max_length=86, blank=True, null=True)
    effect28value = models.CharField(max_length=86, blank=True, null=True)
    effect29type = models.CharField(max_length=86, blank=True, null=True)
    effect29name = models.CharField(max_length=86, blank=True, null=True)
    effect29value = models.CharField(max_length=86, blank=True, null=True)
    effect30type = models.CharField(max_length=86, blank=True, null=True)
    effect30name = models.CharField(max_length=86, blank=True, null=True)
    effect30value = models.CharField(max_length=86, blank=True, null=True)
    effect31type = models.CharField(max_length=86, blank=True, null=True)
    effect31name = models.CharField(max_length=86, blank=True, null=True)
    effect31value = models.CharField(max_length=86, blank=True, null=True)
    effect32type = models.CharField(max_length=86, blank=True, null=True)
    effect32name = models.CharField(max_length=86, blank=True, null=True)
    effect32value = models.CharField(max_length=86, blank=True, null=True)
    actionbarallowed = models.IntegerField(db_column='actionBarAllowed')  # Field name made lowercase.
    enchant_profile_id = models.IntegerField()
    weapon_profile_id = models.IntegerField()
    auctionhouse = models.IntegerField(db_column='auctionHouse')  # Field name made lowercase.
    skillexp = models.IntegerField(db_column='skillExp')  # Field name made lowercase.
    gear_score = models.IntegerField()
    weight = models.IntegerField()
    durability = models.IntegerField()
    autoattack = models.IntegerField()
    socket_type = models.CharField(max_length=86)
    ammotype = models.IntegerField()
    death_loss = models.IntegerField()
    parry = models.IntegerField()
    oadelete = models.IntegerField()
    passive_ability = models.IntegerField()
    shopslots = models.IntegerField(db_column='shopSlots')  # Field name made lowercase.
    shopmodel = models.CharField(db_column='shopModel', max_length=256, db_comment='not use')  # Field name made lowercase.
    shoptag = models.CharField(db_column='shopTag', max_length=256)  # Field name made lowercase.
    numshops = models.IntegerField(db_column='numShops')  # Field name made lowercase.
    shopdestroyonlogout = models.IntegerField(db_column='shopDestroyOnLogOut')  # Field name made lowercase.
    shopmobtemplate = models.IntegerField(db_column='shopMobTemplate')  # Field name made lowercase.
    shoptimeout = models.IntegerField(db_column='shopTimeOut')  # Field name made lowercase.
    repairable = models.IntegerField(blank=True, null=True)
    ground_prefab = models.CharField(max_length=128)
    audio_profile_id = models.IntegerField()
    isactive = models.IntegerField(blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'item_templates'