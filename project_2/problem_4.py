import hashlib
class Helper:
    @staticmethod
    def calc_hash(input_str):
        sha = hashlib.sha256()
        sha.update(input_str.encode('utf-8'))
        return sha.hexdigest()

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = dict()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        key_code = Helper.calc_hash(user)
        self.users[key_code] = user

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    if group == None or user == None or len(user) == 0:
        return False
    sub_groups = group.get_groups()
    key_code =  Helper.calc_hash(user)
    if key_code in group.get_users():
        return True
    elif len(sub_groups) == 0:
        return False
    else:
        for sub_group in sub_groups:
            if is_user_in_group(user, sub_group) == True:
                return True
        return False

parent = Group("parent")
child_1 = Group("child_0")
child_0 = Group("child_1")
child_user_0 = "child_user_0"
child_0.add_user(child_user_0)

sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child_user_2 = "sub_child_user_2"
sub_child.add_user(sub_child_user_2)
child_1.add_group(sub_child)

parent.add_group(child_0)
parent.add_group(child_1)

test_user = "sub_child_user_2"
test_groups = [parent, child_0, child_1, sub_child]
expected_test_results = [True, False, True, True]
for index in range(len(test_groups)):
    test_group = test_groups[index]
    actual_result = is_user_in_group(test_user, test_group)
    passed = expected_test_results[index] == actual_result
    message = 'Passed' if passed else 'Failed'
    print('Test for user ' + test_user + ', Group: ' +  test_group.get_name() + ', '+ message )
    
ans = is_user_in_group('child_user_0', parent)
#  should be True
print(ans)
ans = is_user_in_group('Wrong user', parent)
#  should be False
print(ans)
#  wrong user
ans = is_user_in_group('Not in any group', parent)
#  should be False
print(ans)
#  empty user
ans = is_user_in_group('', child_0)
#  should be False
print(ans)

#  wrong user
ans = is_user_in_group('child_user_0', child_1)
#  should be False
print(ans)
