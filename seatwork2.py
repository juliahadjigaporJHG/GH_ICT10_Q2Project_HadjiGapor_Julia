# Stuent Club Member Checker
from pyscript import display, document


def student_club(e):
    document.getElementById('result').innerHTML = ' '
    first_name =  document.getElementById('first_name').value
    soccer_member = ['Rin', 'Yoichi', 'Hyoma', 'Seishiro', 'Meguru', 'Eita', 'Kenyu']
    member_checker = first_name in soccer_member
    
    last_name =  document.getElementById('last_name').value
    soccer_member = ['Itoshi', 'Isagi', 'Chigiri', 'Nagi', 'Bachira', 'Otoya', 'Yukimiya']
    member_checker = last_name in soccer_member
    
    display_message = (f'Sorry, you are not qualified enough to join our team. Practice more', f'Congratulations {first_name} {last_name}, you are now part of the Blue Lock soccer varsity! Let us learn and imrove together as a team. Check your email to see your schedule and for more information about us.')

    display(display_message[member_checker], target='result')