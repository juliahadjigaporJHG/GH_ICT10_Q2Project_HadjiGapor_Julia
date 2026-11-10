#Drill 2
from pyscript import document



def new_members(e):
    document.getElementById("result").innerHTML = ""
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value
    member_set1 = {'Rin Itoshi', 'Yoichi Isagi'}
    member_set2 = {'Seishiro Nagi', 'Kenyu Yukimiya'}
    member_set3 = {'Meguru Bachira', 'Hyoma Chigiri'}
    member_set4 = {'Eita Otoya', 'Ryusei Shidou'}
    members = member_set1 | member_set2 | member_set3 | member_set4
    new_member = first + " " + last
    members.add(new_member)
    document.getElementById("result").innerHTML = (f"{members} Total Members: {len(members)}")
