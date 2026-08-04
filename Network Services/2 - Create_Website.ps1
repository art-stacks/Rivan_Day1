# ----------------------------
#  VARIABLES
# ----------------------------
$Monitor = "11"

$SLD = "rivan"
$TLD = "com"
$ZoneName = "$SLD$Monitor.$TLD"

# ----------------------------
#  CREATE WEBSITE
# ----------------------------

New-Website -Name $ZoneName -hostheader "www.$ZoneName" -physicalpath "d:\webs\datingbiz"
