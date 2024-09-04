# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountAdmin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=228, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    last_login = models.DateTimeField()
    character_slots = models.IntegerField()
    coin_current = models.IntegerField()
    coin_total = models.IntegerField(blank=True, null=True)
    coin_used = models.IntegerField()
    islands_available = models.IntegerField()
    last_logout = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'account'


class AccountCharacter(models.Model):
    characterid = models.BigIntegerField(db_column='characterId', primary_key=True)  # Field name made lowercase.
    charactername = models.CharField(db_column='characterName', max_length=45)  # Field name made lowercase.
    accountid = models.BigIntegerField(db_column='accountId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account_character'


class AccountPurchases(models.Model):
    account_id = models.BigIntegerField()
    itemid = models.IntegerField(db_column='itemID', blank=True, null=True)  # Field name made lowercase.
    itempurchasedate = models.DateTimeField(db_column='itemPurchaseDate')  # Field name made lowercase.
    itemclaims = models.TextField(db_column='itemClaims', blank=True, null=True)  # Field name made lowercase.
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_purchases'


class AchivementData(models.Model):
    playeroid = models.BigIntegerField(db_column='playerOid')  # Field name made lowercase.
    type = models.IntegerField()
    obj = models.CharField(max_length=200)
    rankingid = models.IntegerField(db_column='rankingId')  # Field name made lowercase.
    achievementid = models.IntegerField(db_column='achievementId')  # Field name made lowercase.
    acquired = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'achivement_data'


class AuctionHouse(models.Model):
    startbid = models.BigIntegerField()
    currency_id = models.IntegerField()
    expire_date = models.DateTimeField()
    auctioneer_oid = models.BigIntegerField()
    owner_oid = models.BigIntegerField()
    bidder_oid = models.BigIntegerField()
    race_group_id = models.IntegerField()
    bid = models.IntegerField()
    buyout = models.BigIntegerField()
    status = models.IntegerField()
    mode = models.IntegerField()
    item_oid = models.BigIntegerField()
    item_count = models.IntegerField()
    item_template_id = models.IntegerField()
    item_enchant_level = models.IntegerField()
    item_sockets_info = models.TextField()
    world_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'auction_house'


class AuctionHouseEnded(models.Model):
    id = models.BigAutoField(primary_key=True)
    startbid = models.IntegerField()
    currency_id = models.IntegerField()
    expire_date = models.DateTimeField()
    auctioneer_oid = models.BigIntegerField()
    owner_oid = models.BigIntegerField()
    bidder_oid = models.BigIntegerField()
    race_group_id = models.IntegerField()
    bid = models.IntegerField()
    buyout = models.BigIntegerField()
    status = models.IntegerField()
    mode = models.IntegerField()
    item_oid = models.BigIntegerField()
    item_count = models.IntegerField()
    item_template_id = models.IntegerField()
    item_enchant_level = models.IntegerField()
    item_sockets_info = models.TextField()
    world_name = models.CharField(max_length=64)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auction_house_ended'


class CharacterBlockList(models.Model):
    character_id = models.BigIntegerField()
    block_player_id = models.BigIntegerField()
    friend_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'character_block_list'


class CharacterFriends(models.Model):
    character_id = models.BigIntegerField()
    friend_id = models.BigIntegerField()
    friend_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'character_friends'


class CharacterMail(models.Model):
    mailid = models.AutoField(db_column='mailId', primary_key=True)  # Field name made lowercase.
    mailarchive = models.IntegerField(db_column='mailArchive')  # Field name made lowercase.
    isaccountmail = models.IntegerField(db_column='isAccountMail')  # Field name made lowercase.
    recipientid = models.BigIntegerField(db_column='recipientId')  # Field name made lowercase.
    recipientname = models.CharField(db_column='recipientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    senderid = models.BigIntegerField(db_column='senderId')  # Field name made lowercase.
    sendername = models.CharField(db_column='senderName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mailread = models.IntegerField(db_column='mailRead')  # Field name made lowercase.
    mailsubject = models.CharField(db_column='mailSubject', max_length=255, db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    mailmessage = models.TextField(db_column='mailMessage', db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    currencytype = models.IntegerField(db_column='currencyType', blank=True, null=True)  # Field name made lowercase.
    currencyamount = models.BigIntegerField(db_column='currencyAmount', blank=True, null=True)  # Field name made lowercase.
    currencytaken = models.IntegerField(db_column='currencyTaken', blank=True, null=True)  # Field name made lowercase.
    cod = models.IntegerField(db_column='CoD')  # Field name made lowercase.
    mailattachmentitemid1taken = models.IntegerField(db_column='mailAttachmentItemId1Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid1 = models.BigIntegerField(db_column='mailAttachmentItemId1', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid2taken = models.IntegerField(db_column='mailAttachmentItemId2Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid2 = models.BigIntegerField(db_column='mailAttachmentItemId2', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid3taken = models.IntegerField(db_column='mailAttachmentItemId3Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid3 = models.BigIntegerField(db_column='mailAttachmentItemId3', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid4taken = models.IntegerField(db_column='mailAttachmentItemId4Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid4 = models.BigIntegerField(db_column='mailAttachmentItemId4', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid5taken = models.IntegerField(db_column='mailAttachmentItemId5Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid5 = models.BigIntegerField(db_column='mailAttachmentItemId5', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid6taken = models.IntegerField(db_column='mailAttachmentItemId6Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid6 = models.BigIntegerField(db_column='mailAttachmentItemId6', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid7taken = models.IntegerField(db_column='mailAttachmentItemId7Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid7 = models.BigIntegerField(db_column='mailAttachmentItemId7', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid8taken = models.IntegerField(db_column='mailAttachmentItemId8Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid8 = models.BigIntegerField(db_column='mailAttachmentItemId8', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid9taken = models.IntegerField(db_column='mailAttachmentItemId9Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid9 = models.BigIntegerField(db_column='mailAttachmentItemId9', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid10taken = models.IntegerField(db_column='mailAttachmentItemId10Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid10 = models.BigIntegerField(db_column='mailAttachmentItemId10', blank=True, null=True)  # Field name made lowercase.
    expiry = models.DateTimeField(blank=True, null=True)
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='dateUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'character_mail'


class CharacterPurchases(models.Model):
    character_id = models.BigIntegerField()
    itemid = models.IntegerField(db_column='itemID', blank=True, null=True)  # Field name made lowercase.
    itempurchasedate = models.DateTimeField(db_column='itemPurchaseDate')  # Field name made lowercase.
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_purchases'


class ChatLogs(models.Model):
    world = models.CharField(max_length=50)
    date = models.DateTimeField()
    message = models.TextField(db_collation='utf8mb4_general_ci')
    source = models.BigIntegerField()
    target = models.BigIntegerField()
    channel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chat_logs'


class Claim(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    instance = models.IntegerField()
    instanceowner = models.BigIntegerField(db_column='instanceOwner')  # Field name made lowercase.
    instanceguild = models.BigIntegerField(db_column='instanceGuild')  # Field name made lowercase.
    locx = models.FloatField(db_column='locX')  # Field name made lowercase.
    locy = models.FloatField(db_column='locY')  # Field name made lowercase.
    locz = models.FloatField(db_column='locZ')  # Field name made lowercase.
    claimtype = models.IntegerField(db_column='claimType')  # Field name made lowercase.
    owner = models.BigIntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    sizez = models.IntegerField(db_column='sizeZ', blank=True, null=True)  # Field name made lowercase.
    sizey = models.IntegerField(db_column='sizeY', blank=True, null=True)  # Field name made lowercase.
    forsale = models.IntegerField(db_column='forSale', blank=True, null=True)  # Field name made lowercase.
    sellername = models.CharField(db_column='sellerName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cost = models.BigIntegerField(blank=True, null=True)
    currency = models.IntegerField(blank=True, null=True)
    purchaseitemreq = models.CharField(db_column='purchaseItemReq', max_length=45, blank=True, null=True)  # Field name made lowercase.
    taxpaiduntil = models.DateTimeField(db_column='taxPaidUntil', blank=True, null=True)  # Field name made lowercase.
    claimitemtemplate = models.IntegerField(db_column='claimItemTemplate', blank=True, null=True)  # Field name made lowercase.
    bonditemtemplate = models.IntegerField(db_column='bondItemTemplate', blank=True, null=True)  # Field name made lowercase.
    bondpaiduntil = models.DateTimeField(db_column='bondPaidUntil', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField()
    upgrade = models.IntegerField()
    parent = models.IntegerField()
    permanent = models.IntegerField()
    org_cost = models.BigIntegerField()
    org_currency = models.IntegerField()
    object_limit_profile = models.IntegerField()
    taxcurrency = models.IntegerField(db_column='taxCurrency')  # Field name made lowercase.
    taxamount = models.BigIntegerField(db_column='taxAmount')  # Field name made lowercase.
    taxinterval = models.BigIntegerField(db_column='taxInterval')  # Field name made lowercase.
    taxperiodpay = models.BigIntegerField(db_column='taxPeriodPay')  # Field name made lowercase.
    taxperiodsell = models.BigIntegerField(db_column='taxPeriodSell')  # Field name made lowercase.
    isactive = models.IntegerField(blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claim'


class ClaimAction(models.Model):
    claimid = models.IntegerField(db_column='claimID', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(max_length=45, blank=True, null=True)
    brushtype = models.CharField(db_column='brushType', max_length=45)  # Field name made lowercase.
    locx = models.FloatField(db_column='locX')  # Field name made lowercase.
    locy = models.FloatField(db_column='locY')  # Field name made lowercase.
    locz = models.FloatField(db_column='locZ')  # Field name made lowercase.
    material = models.SmallIntegerField()
    normalx = models.FloatField(db_column='normalX')  # Field name made lowercase.
    normaly = models.FloatField(db_column='normalY')  # Field name made lowercase.
    normalz = models.FloatField(db_column='normalZ')  # Field name made lowercase.
    sizex = models.FloatField(db_column='sizeX')  # Field name made lowercase.
    sizey = models.FloatField(db_column='sizeY')  # Field name made lowercase.
    sizez = models.FloatField(db_column='sizeZ')  # Field name made lowercase.
    isactive = models.IntegerField(blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claim_action'


class ClaimObject(models.Model):
    claimid = models.IntegerField(db_column='claimID', blank=True, null=True)  # Field name made lowercase.
    template = models.IntegerField(blank=True, null=True)
    stage = models.IntegerField()
    complete = models.IntegerField()
    parent = models.IntegerField(blank=True, null=True)
    parents = models.CharField(max_length=256)
    gameobject = models.CharField(db_column='gameObject', max_length=256, blank=True, null=True)  # Field name made lowercase.
    locx = models.FloatField(db_column='locX', blank=True, null=True)  # Field name made lowercase.
    locy = models.FloatField(db_column='locY', blank=True, null=True)  # Field name made lowercase.
    locz = models.FloatField(db_column='locZ', blank=True, null=True)  # Field name made lowercase.
    orientx = models.FloatField(db_column='orientX', blank=True, null=True)  # Field name made lowercase.
    orienty = models.FloatField(db_column='orientY', blank=True, null=True)  # Field name made lowercase.
    orientz = models.FloatField(db_column='orientZ', blank=True, null=True)  # Field name made lowercase.
    orientw = models.FloatField(db_column='orientW', blank=True, null=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemID', blank=True, null=True)  # Field name made lowercase.
    objectstate = models.CharField(db_column='objectState', max_length=64, blank=True, null=True)  # Field name made lowercase.
    health = models.IntegerField(blank=True, null=True)
    maxhealth = models.IntegerField(db_column='maxHealth', blank=True, null=True)  # Field name made lowercase.
    item1 = models.IntegerField(blank=True, null=True)
    item1count = models.IntegerField(db_column='item1Count', blank=True, null=True)  # Field name made lowercase.
    item2 = models.IntegerField(blank=True, null=True)
    item2count = models.IntegerField(db_column='item2Count', blank=True, null=True)  # Field name made lowercase.
    item3 = models.IntegerField(blank=True, null=True)
    item3count = models.IntegerField(db_column='item3Count', blank=True, null=True)  # Field name made lowercase.
    item4 = models.IntegerField(blank=True, null=True)
    item4count = models.IntegerField(db_column='item4Count', blank=True, null=True)  # Field name made lowercase.
    item5 = models.IntegerField(blank=True, null=True)
    item5count = models.IntegerField(db_column='item5Count', blank=True, null=True)  # Field name made lowercase.
    item6 = models.IntegerField(blank=True, null=True)
    item6count = models.IntegerField(db_column='item6Count', blank=True, null=True)  # Field name made lowercase.
    locktemplateid = models.IntegerField(db_column='lockTemplateID', blank=True, null=True)  # Field name made lowercase.
    lockdurability = models.IntegerField(db_column='lockDurability', blank=True, null=True)  # Field name made lowercase.
    start_build_time = models.BigIntegerField()
    progress = models.IntegerField()
    taskcurrenttime = models.BigIntegerField(db_column='taskCurrentTime')  # Field name made lowercase.
    tasklasttimeupdate = models.BigIntegerField(db_column='taskLastTimeUpdate')  # Field name made lowercase.
    ownerstat = models.IntegerField(db_column='ownerStat')  # Field name made lowercase.
    taskplayeroid = models.BigIntegerField(db_column='taskPlayerOid')  # Field name made lowercase.
    finalstage = models.IntegerField(db_column='finalStage')  # Field name made lowercase.
    isactive = models.IntegerField(blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claim_object'


class ClaimPermission(models.Model):
    claimid = models.IntegerField(db_column='claimID')  # Field name made lowercase.
    playeroid = models.BigIntegerField(db_column='playerOid', blank=True, null=True)  # Field name made lowercase.
    playername = models.CharField(db_column='playerName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    permissionlevel = models.IntegerField(db_column='permissionLevel', blank=True, null=True)  # Field name made lowercase.
    dategiven = models.DateTimeField(db_column='dateGiven', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claim_permission'


class ClaimResource(models.Model):
    claimid = models.IntegerField(db_column='claimID')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemID')  # Field name made lowercase.
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'claim_resource'


class ClaimUpgrade(models.Model):
    claimid = models.IntegerField(db_column='claimID')  # Field name made lowercase.
    locx = models.FloatField(db_column='locX')  # Field name made lowercase.
    locy = models.FloatField(db_column='locY')  # Field name made lowercase.
    locz = models.FloatField(db_column='locZ')  # Field name made lowercase.
    sizex = models.IntegerField(db_column='sizeX', blank=True, null=True)  # Field name made lowercase.
    sizez = models.IntegerField(db_column='sizeZ', blank=True, null=True)  # Field name made lowercase.
    sizey = models.IntegerField(db_column='sizeY', blank=True, null=True)  # Field name made lowercase.
    cost = models.BigIntegerField(blank=True, null=True)
    currency = models.IntegerField(blank=True, null=True)
    purchaseitemreq = models.CharField(db_column='purchaseItemReq', max_length=45, blank=True, null=True)  # Field name made lowercase.
    object_limit_profile = models.IntegerField()
    taxcurrency = models.IntegerField(db_column='taxCurrency')  # Field name made lowercase.
    taxamount = models.BigIntegerField(db_column='taxAmount')  # Field name made lowercase.
    taxinterval = models.BigIntegerField(db_column='taxInterval')  # Field name made lowercase.
    taxperiodpay = models.BigIntegerField(db_column='taxPeriodPay')  # Field name made lowercase.
    taxperiodsell = models.BigIntegerField(db_column='taxPeriodSell')  # Field name made lowercase.
    isactive = models.IntegerField(blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claim_upgrade'


class Cooldowns(models.Model):
    cid = models.CharField(max_length=100)
    duration = models.IntegerField()
    starttime = models.BigIntegerField(db_column='startTime')  # Field name made lowercase.
    obj_oid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cooldowns'


class DataLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    world_name = models.CharField(max_length=64)
    data_name = models.CharField(max_length=64)
    data_timestamp = models.DateTimeField()
    source_oid = models.BigIntegerField()
    target_oid = models.BigIntegerField()
    account_id = models.BigIntegerField()
    additional_data = models.TextField(blank=True, null=True)
    process_timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data_logs'


class Guild(models.Model):
    name = models.CharField(max_length=45)
    faction = models.IntegerField()
    motd = models.CharField(max_length=256)
    omotd = models.CharField(max_length=256)
    isactive = models.IntegerField(blank=True, null=True)
    level = models.SmallIntegerField()
    warehouse = models.BigIntegerField()
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'guild'


class GuildLevelResources(models.Model):
    guild_id = models.IntegerField()
    item_id = models.IntegerField()
    item_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guild_level_resources'


class GuildMember(models.Model):
    guildid = models.IntegerField(db_column='guildID')  # Field name made lowercase.
    memberoid = models.BigIntegerField(db_column='memberOid')  # Field name made lowercase.
    name = models.CharField(max_length=32, blank=True, null=True)
    guildrank = models.IntegerField(db_column='guildRank', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=128, blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guild_member'


class GuildRank(models.Model):
    guildid = models.IntegerField(db_column='guildID')  # Field name made lowercase.
    guildrank = models.IntegerField(db_column='guildRank')  # Field name made lowercase.
    name = models.CharField(max_length=45)
    permissions = models.CharField(max_length=256)
    creationtimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guild_rank'


class HistoryAuctionHouseEnded(models.Model):
    id = models.BigAutoField(primary_key=True)
    auction_id = models.BigIntegerField()
    startbid = models.IntegerField()
    currency_id = models.IntegerField()
    expire_date = models.DateTimeField()
    auctioneer_oid = models.BigIntegerField()
    owner_oid = models.BigIntegerField()
    bidder_oid = models.BigIntegerField()
    race_group_id = models.IntegerField()
    bid = models.IntegerField()
    buyout = models.BigIntegerField()
    status = models.IntegerField()
    mode = models.IntegerField()
    item_oid = models.BigIntegerField()
    item_count = models.IntegerField()
    item_template_id = models.IntegerField()
    item_enchant_level = models.IntegerField()
    item_sockets_info = models.TextField()
    world_name = models.CharField(max_length=64)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history_auction_house_ended'


class HistoryCharacterMail(models.Model):
    mailid = models.IntegerField(db_column='mailId')  # Field name made lowercase.
    mailarchive = models.IntegerField(db_column='mailArchive')  # Field name made lowercase.
    isaccountmail = models.IntegerField(db_column='isAccountMail')  # Field name made lowercase.
    recipientid = models.BigIntegerField(db_column='recipientId')  # Field name made lowercase.
    recipientname = models.CharField(db_column='recipientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    senderid = models.BigIntegerField(db_column='senderId')  # Field name made lowercase.
    sendername = models.CharField(db_column='senderName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mailread = models.IntegerField(db_column='mailRead')  # Field name made lowercase.
    mailsubject = models.CharField(db_column='mailSubject', max_length=255)  # Field name made lowercase.
    mailmessage = models.TextField(db_column='mailMessage')  # Field name made lowercase.
    currencytype = models.IntegerField(db_column='currencyType', blank=True, null=True)  # Field name made lowercase.
    currencyamount = models.IntegerField(db_column='currencyAmount', blank=True, null=True)  # Field name made lowercase.
    currencytaken = models.IntegerField(db_column='currencyTaken', blank=True, null=True)  # Field name made lowercase.
    cod = models.IntegerField(db_column='CoD')  # Field name made lowercase.
    mailattachmentitemid1taken = models.IntegerField(db_column='mailAttachmentItemId1Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid1 = models.BigIntegerField(db_column='mailAttachmentItemId1', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid2taken = models.IntegerField(db_column='mailAttachmentItemId2Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid2 = models.BigIntegerField(db_column='mailAttachmentItemId2', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid3taken = models.IntegerField(db_column='mailAttachmentItemId3Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid3 = models.BigIntegerField(db_column='mailAttachmentItemId3', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid4taken = models.IntegerField(db_column='mailAttachmentItemId4Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid4 = models.BigIntegerField(db_column='mailAttachmentItemId4', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid5taken = models.IntegerField(db_column='mailAttachmentItemId5Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid5 = models.BigIntegerField(db_column='mailAttachmentItemId5', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid6taken = models.IntegerField(db_column='mailAttachmentItemId6Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid6 = models.BigIntegerField(db_column='mailAttachmentItemId6', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid7taken = models.IntegerField(db_column='mailAttachmentItemId7Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid7 = models.BigIntegerField(db_column='mailAttachmentItemId7', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid8taken = models.IntegerField(db_column='mailAttachmentItemId8Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid8 = models.BigIntegerField(db_column='mailAttachmentItemId8', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid9taken = models.IntegerField(db_column='mailAttachmentItemId9Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid9 = models.BigIntegerField(db_column='mailAttachmentItemId9', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid10taken = models.IntegerField(db_column='mailAttachmentItemId10Taken', blank=True, null=True)  # Field name made lowercase.
    mailattachmentitemid10 = models.BigIntegerField(db_column='mailAttachmentItemId10', blank=True, null=True)  # Field name made lowercase.
    expiry = models.DateTimeField(blank=True, null=True)
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='dateUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'history_character_mail'


class InstanceTemplate(models.Model):
    island_name = models.CharField(unique=True, max_length=64)
    template = models.CharField(max_length=64)
    administrator = models.IntegerField()
    category = models.IntegerField()
    status = models.CharField(max_length=32)
    subscription = models.DateTimeField(blank=True, null=True)
    public = models.IntegerField()
    password = models.CharField(max_length=64)
    rating = models.IntegerField()
    islandtype = models.IntegerField(db_column='islandType')  # Field name made lowercase.
    globalwaterheight = models.FloatField(db_column='globalWaterHeight')  # Field name made lowercase.
    createonstartup = models.IntegerField(db_column='createOnStartup')  # Field name made lowercase.
    style = models.CharField(max_length=64)
    recommendedlevel = models.IntegerField(db_column='recommendedLevel')  # Field name made lowercase.
    description = models.TextField()
    size = models.IntegerField()
    populationlimit = models.IntegerField(db_column='populationLimit')  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='lastUpdate')  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'instance_template'


class IslandDevelopers(models.Model):
    island = models.IntegerField()
    developer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'island_developers'


class IslandFriends(models.Model):
    island = models.IntegerField()
    user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'island_friends'


class IslandPortals(models.Model):
    island = models.IntegerField()
    portaltype = models.IntegerField(db_column='portalType')  # Field name made lowercase.
    faction = models.IntegerField()
    locx = models.DecimalField(db_column='locX', max_digits=65, decimal_places=2)  # Field name made lowercase.
    locy = models.DecimalField(db_column='locY', max_digits=65, decimal_places=2)  # Field name made lowercase.
    locz = models.DecimalField(db_column='locZ', max_digits=65, decimal_places=2)  # Field name made lowercase.
    orientx = models.IntegerField(db_column='orientX')  # Field name made lowercase.
    orienty = models.IntegerField(db_column='orientY')  # Field name made lowercase.
    orientz = models.IntegerField(db_column='orientZ')  # Field name made lowercase.
    orientw = models.IntegerField(db_column='orientW')  # Field name made lowercase.
    displayid = models.IntegerField(db_column='displayID')  # Field name made lowercase.
    name = models.CharField(max_length=32, blank=True, null=True)
    gameobject = models.CharField(db_column='gameObject', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'island_portals'


class MemoryDataStats(models.Model):
    type = models.CharField(unique=True, max_length=45, blank=True, null=True)
    value = models.BigIntegerField(blank=True, null=True)
    world = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memory_data_stats'


class PlayerShop(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_oid = models.BigIntegerField()
    player_oid = models.BigIntegerField()
    tag = models.CharField(max_length=256)
    title = models.CharField(max_length=1024)
    end_player_logout = models.IntegerField()
    createtime = models.BigIntegerField()
    timeout = models.IntegerField()
    player = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_shop'


class PlayerShopItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_oid = models.BigIntegerField()
    item_oid = models.BigIntegerField()
    price = models.BigIntegerField()
    currency = models.IntegerField()
    template_id = models.IntegerField()
    count = models.IntegerField()
    sell = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_shop_items'


class RankingRun(models.Model):
    world = models.CharField(primary_key=True, max_length=50)
    last_run = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ranking_run'


class Rankings(models.Model):
    pos = models.IntegerField()
    player = models.BigIntegerField()
    ranking = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rankings'


class Server(models.Model):
    action = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server'


class ServerStats(models.Model):
    players_online = models.IntegerField(primary_key=True)
    last_login = models.DateTimeField()
    logins_since_restart = models.IntegerField()
    last_restart = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'server_stats'


class ServerStatus(models.Model):
    server = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_status'


class ServerVersion(models.Model):
    server_version = models.CharField(primary_key=True, max_length=10)
    installation_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_version'


class ShopSpawnData(models.Model):
    category = models.IntegerField()
    name = models.CharField(max_length=64)
    mobtemplate = models.IntegerField(db_column='mobTemplate')  # Field name made lowercase.
    mobtemplate2 = models.IntegerField(db_column='mobTemplate2')  # Field name made lowercase.
    mobtemplate3 = models.IntegerField(db_column='mobTemplate3')  # Field name made lowercase.
    mobtemplate4 = models.IntegerField(db_column='mobTemplate4')  # Field name made lowercase.
    mobtemplate5 = models.IntegerField(db_column='mobTemplate5')  # Field name made lowercase.
    markername = models.CharField(db_column='markerName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    locx = models.FloatField(db_column='locX', blank=True, null=True)  # Field name made lowercase.
    locy = models.FloatField(db_column='locY', blank=True, null=True)  # Field name made lowercase.
    locz = models.FloatField(db_column='locZ', blank=True, null=True)  # Field name made lowercase.
    orientx = models.FloatField(db_column='orientX', blank=True, null=True)  # Field name made lowercase.
    orienty = models.FloatField(db_column='orientY', blank=True, null=True)  # Field name made lowercase.
    orientz = models.FloatField(db_column='orientZ', blank=True, null=True)  # Field name made lowercase.
    orientw = models.FloatField(db_column='orientW', blank=True, null=True)  # Field name made lowercase.
    instance = models.IntegerField(blank=True, null=True)
    numspawns = models.IntegerField(db_column='numSpawns', blank=True, null=True)  # Field name made lowercase.
    spawnradius = models.IntegerField(db_column='spawnRadius', blank=True, null=True)  # Field name made lowercase.
    respawntime = models.IntegerField(db_column='respawnTime', blank=True, null=True)  # Field name made lowercase.
    respawntimemax = models.IntegerField(db_column='respawnTimeMax', blank=True, null=True)  # Field name made lowercase.
    corpsedespawntime = models.IntegerField(db_column='corpseDespawnTime', blank=True, null=True)  # Field name made lowercase.
    spawnactivestarthour = models.IntegerField(db_column='spawnActiveStartHour', blank=True, null=True)  # Field name made lowercase.
    spawnactiveendhour = models.IntegerField(db_column='spawnActiveEndHour', blank=True, null=True)  # Field name made lowercase.
    alternatespawnmobtemplate = models.IntegerField(db_column='alternateSpawnMobTemplate')  # Field name made lowercase.
    alternatespawnmobtemplate2 = models.IntegerField(db_column='alternateSpawnMobTemplate2')  # Field name made lowercase.
    alternatespawnmobtemplate3 = models.IntegerField(db_column='alternateSpawnMobTemplate3')  # Field name made lowercase.
    alternatespawnmobtemplate4 = models.IntegerField(db_column='alternateSpawnMobTemplate4')  # Field name made lowercase.
    alternatespawnmobtemplate5 = models.IntegerField(db_column='alternateSpawnMobTemplate5')  # Field name made lowercase.
    combat = models.IntegerField()
    roamradius = models.IntegerField(db_column='roamRadius')  # Field name made lowercase.
    startsquests = models.CharField(db_column='startsQuests', max_length=256)  # Field name made lowercase.
    endsquests = models.CharField(db_column='endsQuests', max_length=256)  # Field name made lowercase.
    startsdialogues = models.CharField(db_column='startsDialogues', max_length=256)  # Field name made lowercase.
    otheractions = models.CharField(db_column='otherActions', max_length=256)  # Field name made lowercase.
    baseaction = models.CharField(db_column='baseAction', max_length=32)  # Field name made lowercase.
    weaponsheathed = models.IntegerField(db_column='weaponSheathed')  # Field name made lowercase.
    merchanttable = models.IntegerField(db_column='merchantTable')  # Field name made lowercase.
    patrolpath = models.IntegerField(db_column='patrolPath')  # Field name made lowercase.
    questopenloottable = models.IntegerField(db_column='questOpenLootTable')  # Field name made lowercase.
    ischest = models.IntegerField(db_column='isChest')  # Field name made lowercase.
    pickupitem = models.IntegerField(db_column='pickupItem', blank=True, null=True)  # Field name made lowercase.
    shop_owner = models.BigIntegerField()
    shop_oid = models.BigIntegerField()
    shop_message = models.CharField(max_length=512)
    isactive = models.IntegerField(blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    updatetimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_spawn_data'


class Shopitems(models.Model):
    name = models.CharField(unique=True, max_length=64)
    cost = models.IntegerField()
    category = models.CharField(max_length=32)
    imageaddress = models.CharField(db_column='imageAddress', max_length=128)  # Field name made lowercase.
    newitem = models.IntegerField(db_column='newItem', blank=True, null=True)  # Field name made lowercase.
    costimage = models.CharField(db_column='costImage', max_length=128, blank=True, null=True)  # Field name made lowercase.
    buyimage = models.CharField(db_column='buyImage', max_length=128, blank=True, null=True)  # Field name made lowercase.
    purchasetype = models.CharField(db_column='purchaseType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    objectname = models.CharField(db_column='objectName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    purchaselimit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopitems'


class Templateportals(models.Model):
    templateid = models.IntegerField(db_column='templateID')  # Field name made lowercase.
    portaltype = models.IntegerField(db_column='portalType')  # Field name made lowercase.
    faction = models.IntegerField()
    locx = models.IntegerField(db_column='locX')  # Field name made lowercase.
    locy = models.IntegerField(db_column='locY')  # Field name made lowercase.
    locz = models.IntegerField(db_column='locZ')  # Field name made lowercase.
    displayid = models.IntegerField(db_column='displayID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'templateportals'


class Templates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'templates'


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'users'


class WorldTime(models.Model):
    world_name = models.CharField(unique=True, max_length=50)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    second = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'world_time'
