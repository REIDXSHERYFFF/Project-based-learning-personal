# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

def main():
    
    revoked_badge_numbers = {'1', '21', '43', '22', '71', '11'}

    approved = []
    denied = []
    visitor_count = 0
    max_visitors = 5
    
    print("Access Control Scanner")
    print("=" * 23)

#    username = input('please enter visitor name(secret code): ')
    
    while visitor_count <= max_visitors:
        username = input('please enter your visitor username:  ')

        if username == 'done':
            break
        badge_number = input("provide your badge number(last 2 digits only): ")

        if badge_number in revoked_badge_numbers:
            denied.append(username)
            visitor_count += 1
            print(f"⛔️USER ACCESS DENIED! YOUR BADGE NUMBER {badge_number} IS REVOKED.")
###     elif username.isdigit != True:
###     denied.append(username)
###     visitor_count += 1
###     print(f"⛔️USER ACCESS DENIED! YOUR BADGE NUMBER {badge_number} IS REVOKED.")
        else:
            approved.append(username)
            visitor_count += 1
            print(f"✅USER ACCESS GRANTED. PLEASE PROCEED {badge_number}")
        
        # Show remaining attempts
        
        remaining = max_visitors - visitor_count
        if remaining > 0:
            print(f"Remaining attempts: {remaining}")
        else:
            print("Maximum visitors reached!")
            break

    print("\n" + "=" * 23)
    print("📊 ACCESS SUMMARY")
    print("=" * 23)


    approved.sort()
    denied.sort()


    if approved:
        for i, username in enumerate(approved):
            print(f'{i}. {username}')                
    else:
        print('no approved visitors')    

    if denied:
        for i,username in enumerate(denied):
            print(f'{i}. {username}')        
    else:
        print('no denied visitors')    

    print(f"✅ approved visitors == {approved} ")
    print(f"⛔️ denied visitors == {denied} ")
    
    print(f"\nSummary Statistics:")
    print(f"   Total Visitors: {len(approved) + len(denied)}")
    print(f"   Approval Rate: {len(approved) / (len(approved) + len(denied)) * 100:.1f}%" if (len(approved) + len(denied)) > 0 else "   Approval Rate: 0.0%")        
          
if __name__ == "__main__":
    main()