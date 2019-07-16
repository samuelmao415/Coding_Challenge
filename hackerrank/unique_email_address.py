email = "test.email@leetcode.com"


len(email.split('+'))

'test'.replace('.','')


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        same_email_count = 0
        email_list = []
        for email in emails:
            if len(email.split('+'))>1: #with + sign in email
                email_domain = email.split('@')[-1]
                user_name = email.split('+')[0].replace('.','')
                clean_email = user_name + '@' + email_domain
                if clean_email not in email_list:
                    email_list.append(clean_email)
            if len(email.split('+'))==1: #without + sign in email
                email_domain = email.split('@')[-1]
                user_name = email.split('@')[0].replace('.', '')
                clean_email = user_name + '@' + email_domain
                if clean_email not in email_list:
                    email_list.append(clean_email)
        print(email_list)
        return(len(email_list))
                    
