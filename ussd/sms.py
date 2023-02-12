import africastalking

username = "sandbox"
api_key="82e31213cb02a4b16b4450227142cb67852f52615d3374066505dfd886e73afa"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

def send_sms(message, recipients):
    try:
        response = sms.send(message , [recipients])
        print(response)
        
    except Exception as e:
        import traceback
        print('Encountered an error while sending: %s' % str(e))
        print(traceback.format_exc())