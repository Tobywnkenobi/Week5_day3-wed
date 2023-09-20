# How to solve a problem:

#     -Figure out wher the input and its type are
#     -Set up a function
#     -Figure out what the output and its type are
#     -Gather your Knowledge
#     -Gathers your contraints (Not Always Necessary)
#     -Determine a Logical way to solve the problem
#      -Write each step out in English
#       -Write each step out in Python-esse (sudo-code)
#       -Invoke and Test your function

'''
# DESCRIPTION:
# Given two Arrays in which values are the power of each soldier, return true if you survive the attack or false if you perish.

# CONDITIONS

# Each soldier attacks the opposing soldier in the same index of the array. The survivor is the number with the highest value.
# If the value is the same they both perish
# If one of the values is empty(different array lengths) the non-empty value soldier survives.
# To survive the defending side must have more survivors than the attacking side.
# In case there are the same number of survivors in both sides, the winner is the team with the highest initial attack power. If the total attack power of both sides is the same return true.
# The initial attack power is the sum of all the values in each array.
# EXAMPLES

# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 6, 8 ]
# 0 survivors                4 survivors
# return true


# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4 ]
# 2 survivors  (16 damage)   2 survivors (6 damage)
# return false

# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 0, 8 ]
# 1 survivors                3 survivors
# return true
'''
#initialize two variables, set to zero to start the battle
# def survival(attackers, defenders):
#     attacker_survivors = 0
#     defender_survivors = 0
# #Need to determine the survivors from both arrays to determine the survivor
#     for a, d in zip(attackers, defenders):
#         if a > d:
#             attacker_survivors += 1
#         elif a < d:
#             defender_survivors += 1
# #If they have different lengths, we have to increment the survivor count
#     if len(attackers) > len(defenders):
#         attacker_survivors += len(attackers) - len(defenders)
#     elif len(attackers) < len(defenders) - len(attackers):
# #compare the number of survivors
#         if defender_survivors > attacker_survivors:
#             return True
#         elif defender_survivors == attacker_survivors:
#             return sum(defenders) >= sum(attackers)
#         else:
#             return False
# #test

# test_cases = [
#     ([1, 3, 5, 7], [2, 4, 6, 8], True),
#     ([1, 3, 5, 7], [2, 4], False),
#     ([1, 3, 5, 7], [2, 4, 0, 8], True)
# ]

# answer = []
# for attackers, defenders, expected in test_cases:
#     answer.append((attackers, defenders, survival(attackers, defenders) == expected))

# print(answer)

# def war(alist_1, alist_2):
#     attackers_survivors = 0
#     defenders_survivors = 0
#     sum_survivors = sum(alist_1)
#     sum_defenders = sum(alist_2)
#     while len(alist_1) < len(alist_2):
#         alist_1.append(0)
#     while len(alist_2) < len(alist_1):
#         alist_2.append(0)
#     alist_3 = alist_1 + alist_2
#     k = len(alist_3)//2
#     right_point = k
#     left_point = 0
#     while right_point <= len(alist_3)-1:
#         if alist_3[left_point] < alist_3[right_point]:
#             defenders_survivors += 1
#             left_point += 1
#             right_point += 1
#         elif alist_3[right_point] < alist_3[left_point]:
#             attackers_survivors += 1
#             right_point += 1
#             left_point += 1
#         else:
#             pass
#     print(f"(ATK Survivors: {attackers_survivors}, DEF Survivors: {defenders_survivors}, ATK sum: {sum_survivors}, DEF sum: {sum_defenders})")
#     if defenders_survivors == attackers_survivors:
#         if sum_survivors > sum_defenders:
#             return False
#         elif sum_survivors < sum_defenders:
#             return True
#         else:
#             return True
#     elif defenders_survivors > attackers_survivors:
#         return True
#     elif defenders_survivors < attackers_survivors:
#         return False


def check_surv(alist, alist2):
    def_surv = 0 -> O(1)
    atk_surv = 0 -> O(1)
    atk_power = sum(alist)
    def_power = sum(alist2)
    compare_list = list(zip_longest(alist ,alist2))
    for atk, def_ in compare_list:
        if def_ is None: 
            atk_surv += 1
            continue  
        elif atk is None: 
            def_surv += 1 
            continue 
        if atk > def_: 
            atk_surv += 1 
        elif atk < def_: 
            def_surv += 1 
    if atk_surv > def_surv: 
        return False 
    elif def_surv > atk_surv: 
        return True 
    elif atk_surv == def_surv:
        if atk_power > def_power: 
            return False 
        else: 
            return True