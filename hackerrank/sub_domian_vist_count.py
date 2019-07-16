cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]


def subdomainVisits(cpdomains)
    bin_ = []
    for num_domain in cpdomains:
        num_and_domain = num_domain.split(' ')
        if len(num_and_domain[1].split('.'))>=3:
            num_and_domain_split = num_and_domain[1].split('.')
            parent_domain_one = num_and_domain_split[-2] + '.' + num_and_domain_split[-1]
            parent_domain_two =  num_and_domain_split[-1]
            num_and_domain.append(parent_domain_one)
            num_and_domain.append(parent_domain_two)
        else:
            num_and_domain_split = num_and_domain[1].split('.')
            parent_domain_two =  num_and_domain_split[-1]
            num_and_domain.append(parent_domain_two)
        bin_.append(num_and_domain)
    bin_
    bin_dict = {}
    for websites in bin_:
        for web in websites[1:]:
            if bin_dict.get(web):
                bin_dict[web] = bin_dict[web] + int(websites[0])
            else:
                bin_dict[web] = int(websites[0])
            print(web,websites[0])

    bin_dict
    output = []
    for pair in bin_dict.items():
        output.append(str(pair[1]) + ' ' + pair[0])

    return(output)
