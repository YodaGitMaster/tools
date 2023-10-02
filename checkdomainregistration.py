import whois

names = ['Profy', 'Netpulse', 'Connexa', 'LinkedUp', 'TweedIn', 'Sociafy', 'Interly', 'Bizchat', 'Communit', 'Linkity', 'Workhub', 'TwitNet', 'Engagio', 'Connectr', 'Sociate', 'Profnet', 'Tweetly', 'LinkedUp', 'Collabz', 'Invisio', 'Netcomm', 'Tweetin', 'Netlead', 'Socibus', 'Workmix', 'Linkcom', 'Buzznet', 'Interact', 'Joblink', 'Worknet']
for name in names:
    domain = name + '.com'
    try:
        w = whois.whois(domain)
        if not w.status:
            print(f'{domain} is available!')
        else:
            print(f'{domain} is already taken.')
    except Exception as e:
        print(f'Error: {e}')