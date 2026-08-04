# ----------------------------
#  INSTALL DNS
# ----------------------------
# Install-WindowsFeature -name DNS -IncludeManagementTool
# Install-WindowsFeature -name Web-Server -IncludeManagementTools


# ----------------------------
#  VARIABLES
# ----------------------------
$Monitor = "11"

$ServerIP = "10"

$SLD = "rivan"
$TLD = "com"
$ZoneName = "$SLD$Monitor.$TLD"

$ClassMonitors = @(
    "11"
    "12"
    "21"
    "22"
    "31"
    "32"
    "41"
    "42"
    "51"
    "52"
    "61"
    "62"
    "71"
    "72"
    "81"
    "82"
    "91"
    "92"
)

# List of other DNS Server IPs
$NotifyList = @()
foreach ($record in $ClassMonitors) {
    if ($Monitor -ne $record) {
        $NotifyList += "10.$record.1.$ServerIP"
    }
}

# ReverseLookup
$NetworkID_1 = "10.$Monitor.1.0/24"
$NetworkID_10 = "10.$Monitor.10.0/24"
$NetworkID_50 = "10.$Monitor.50.0/24"
$NetworkID_100 = "10.$Monitor.100.0/24"
$NetworkID_ = "10.$Monitor.$Monitor.0/24"

$RevZoneName_1 = "1.$Monitor.10.in-addr.arpa"
$RevZoneName_10 = "10.$Monitor.10.in-addr.arpa"
$RevZoneName_50 = "50.$Monitor.10.in-addr.arpa"
$RevZoneName_100 = "100.$Monitor.10.in-addr.arpa"
$RevZoneName_ = "$Monitor.$Monitor.10.in-addr.arpa"


# ----------------------------
#  DNS FORWARD LOOKUP ZONE
# ----------------------------

# PRIMARY
Add-DnsServerPrimaryZone -name $ZoneName -ZoneFile "$ZoneName.dns" -DynamicUpdate NonSecureAndSecure


# ----------------------------
#  DNS REVERSE LOOKUP ZONE
# ----------------------------

# ReverseLookupZone
Add-DnsServerPrimaryZone -NetworkId $NetworkID_1 -ZoneFile $RevZoneName_1 -DynamicUpdate NonSecureAndSecure
Add-DnsServerPrimaryZone -NetworkId $NetworkID_10 -ZoneFile $RevZoneName_10 -DynamicUpdate NonSecureAndSecure
Add-DnsServerPrimaryZone -NetworkId $NetworkID_50 -ZoneFile $RevZoneName_50 -DynamicUpdate NonSecureAndSecure
Add-DnsServerPrimaryZone -NetworkId $NetworkID_100 -ZoneFile $RevZoneName_100 -DynamicUpdate NonSecureAndSecure
Add-DnsServerPrimaryZone -NetworkId $NetworkID_ -ZoneFile $RevZoneName_ -DynamicUpdate NonSecureAndSecure


# ----------------------------
#  DNS RECORDS
# ----------------------------
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "@" -IPv4Address "10.$Monitor.1.$ServerIP" -CreatePTR
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "ns" -IPv4Address "10.$Monitor.1.$ServerIP" -CreatePTR

Add-DnsServerResourceRecord -ZoneName $ZoneName -CName -Name "www" -HostName "$ZoneName"
Add-DnsServerResourceRecord -ZoneName $ZoneName -CName -Name "imap" -HostName "$ZoneName"
Add-DnsServerResourceRecord -ZoneName $ZoneName -CName -Name "pop" -HostName "$ZoneName"
Add-DnsServerResourceRecord -ZoneName $ZoneName -CName -Name "smtp" -HostName "$ZoneName"

Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "mail" -IPv4Address "10.$Monitor.1.$ServerIP"
Add-DnsServerResourceRecord -ZoneName $ZoneName -MX -Name "@" -MailExchange "mail.$ZoneName" -Preference 10

# Day1 Devices
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "ct" -IPv4Address "10.$Monitor.1.2" -CreatePTR
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "cb" -IPv4Address "10.$Monitor.1.4" -CreatePTR
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "cm" -IPv4Address "10.$Monitor.100.8" -CreatePTR
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "ed" -IPv4Address "10.$Monitor.$Monitor.1" -CreatePTR
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "p1" -IPv4Address "10.$Monitor.100.101" -CreatePTR
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "p2" -IPv4Address "10.$Monitor.100.102" -CreatePTR
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "c1" -IPv4Address "10.$Monitor.50.6" -CreatePTR
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "c2" -IPv4Address "10.$Monitor.50.8" -CreatePTR
Add-DnsServerResourceRecord -ZoneName $ZoneName -A -Name "ap" -IPv4Address "10.$Monitor.10.3" -CreatePTR


# ----------------------------
#  DNS SECONDARY ZONE
# ----------------------------

# SECONDARY
foreach ($Record in $ClassMonitors) {
    if ($Record -ne $Monitor) {
        Add-DnsServerSecondaryZone -Name "$SLD$Record.$TLD" -ZoneFile "$SLD$Record.$TLD.dns" -MasterServers "10.$Record.1.$ServerIP"
    }
}

# Modify Zone Transfer

Set-DnsServerPrimaryZone -name $ZoneName -SecureSecondaries TransferAnyServer -Notify NotifyServers -NotifyServers $NotifyList
