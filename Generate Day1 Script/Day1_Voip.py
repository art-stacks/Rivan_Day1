
name = input('What is your nickname? ')
monitor = input('What is your monitor number? ')
yourmac = input('''What is the MAC ADDRESS of your mobile phone? 
                
Make sure the mac is not set to randomized, and is in dotted decimal format.
                example.
                1234.1234.1234
                
> ''')

anothermac = input('''What is the MAC ADDRESS of the next person's mobile phone? 
                
Make sure the mac is not set to randomized, and is in dotted decimal format.
                example.
                1234.1234.1234
                   
> ''')


with open(f'day1-voip-{name}-{monitor}.txt', 'w') as file:
    file.write(f'''

! Monitor Num:    {monitor}
! YourPhone Mac:  {yourmac}
! OtherPhone Mac: {anothermac}

************** VOIP Services **************

!@cucm - Interactive Voice Response System
config t
dial-peer voice 69 voip
 service rivanaa out-bound
 destination-pattern {monitor}69
 session target ipv4:10.{monitor}.100.8
 incoming called-number {monitor}69
 dtmf-relay h245-alphanumeric
 codec g711ulaw
 no vad
!
telephony-service
 moh "flash:/en_bacd_music_on_hold.au"
!
application
 service rivanaa flash:app-b-acd-aa-3.0.0.2.tcl
  paramspace english index 1        
  param number-of-hunt-grps 2
  param dial-by-extension-option 8
  param handoff-string rivanaa
  param welcome-prompt flash:en_bacd_welcome.au
  paramspace english language en
  param call-retry-timer 15
  param service-name rivanqueue
  paramspace english location flash:
  param second-greeting-time 60
  param max-time-vm-retry 2
  param voice-mail 1234
  param max-time-call-retry 700
  param aa-pilot {monitor}69
 service rivanqueue flash:app-b-acd-3.0.0.2.tcl
  param queue-len 15
  param aa-hunt1 {monitor}00
  param aa-hunt2 {monitor}77
  param aa-hunt3 {monitor}01
  param aa-hunt4 {monitor}33
  param queue-manager-debugs 1
  param number-of-hunt-grps 4
  end


!@cucm - Session Initiation Protocol
conf t
 voice service voip
  allow-connections h323 to sip
          
  allow-connections sip to h323
  allow-connections sip to sip
  supplementary-service h450.12
 sip
   bind control source-interface fa0/0
   bind media source-interface fa0/0
   registrar server expires max 600 min 60
 voice register global
  mode cme
  source-address 10.{monitor}.100.8 port 5060
  max-dn 12
  max-pool 12
  authenticate register
  create profile sync syncinfo.xml
 voice register dn 1
   number {monitor}69
   allow watch
   name {monitor}69
 voice register dn 2
   number {monitor}70
   allow watch
   name {monitor}70
  voice register pool 1
    id mac {yourmac}
    number 1 dn 1
    dtmf-relay sip-notify
    username {monitor}69 password {monitor}69
    codec g711ulaw
  voice register pool 2
    id mac {anothermac}
    number 1 dn 2
    dtmf-relay sip-notify
    username {monitor}70 password {monitor}70
    codec g711ulaw
	end

               ''')

print(f'''
Script generation complete!
View the file \'day1-voip-{name}-{monitor}.txt\'
''')
