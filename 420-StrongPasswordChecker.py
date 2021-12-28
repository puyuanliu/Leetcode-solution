import re

class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        # Number of steps required to solve rare-word problem
        minimum_rare_word_steps = 0  
        if len(re.findall(r'[a-z]', password)) ==0:
            minimum_rare_word_steps += 1
        if len(re.findall(r'[A-Z]', password)) == 0:
            minimum_rare_word_steps += 1
        if len(re.findall(r'[0-9]', password)) == 0:
            minimum_rare_word_steps += 1
        
        # Number of three-words pattern 
        minimum_repeated_word_steps = len(re.findall(r'(\S)\1{2}', password))
        
        # We split into three cases
        if len(password) <6:
            # Add can solve short, rare-word and repetitive words in this case.
            minimum_add_steps = 6-len(password)  
            return max(minimum_add_steps, minimum_rare_word_steps, minimum_repeated_word_steps)
        
        elif len(password) > 20:
            # We need both delete and replace in this case 
            total_deletes = len(password)-20
            repeated_match = [m for m in re.finditer(r"(\S)\1{2,}", password)] 
            get_clause_length = lambda m : m.span()[1]-m.span()[0] # length of the consequtive repetitions. 
            remaining_delete = total_deletes
            remaining_repeat_steps = minimum_repeated_word_steps
            def my_helper(k):
                nonlocal remaining_delete, remaining_repeat_steps
                num_efficient_delete = len([m for m in repeated_match if get_clause_length(m) % 3 == k])
                consumed_delete = (k+1)*min(remaining_delete//(k+1), num_efficient_delete)
                remaining_repeat_steps = remaining_repeat_steps-consumed_delete//(k+1)
                remaining_delete -= consumed_delete 
            test_list = [0,1]
            for i in test_list:
                my_helper(i)
                if remaining_delete == 0:
                    # no delete action remains 
                    return total_deletes + max(minimum_rare_word_steps, remaining_repeat_steps)
            consumed_delete = 3*min(remaining_delete//3, remaining_repeat_steps)
            remaining_repeat_steps = remaining_repeat_steps-consumed_delete//3
            return total_deletes + max(minimum_rare_word_steps, remaining_repeat_steps)
        else:
            # Replace can solve rare-word and repetitive word issues. 
            return max(minimum_rare_word_steps, minimum_repeated_word_steps)
