#import sqlite3 liberies
import sqlite
conn = sqlite3.connect('youtube_manager.db')
 
cursor = conn.cursor()

cursor.execute('''
    create table if not exists videos (
                id integer primary key, 
                name text NOT NULL, 
                time text NOT NULL
    )
''')

def list_videos():
    cursor.execute('select * from videos')
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    cursor.execute("insert into videos (name, time) values(?, ?)", (name, time))
    conn.commit()

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? where id = ?", (
        new_name, new_time, video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("delete from videos where id  = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\n<<<<< Youtube Manager App Through Sqllite3 >>>>>")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        choice = input("Enter Your Choice : ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter the movie name : ")
            time = input("Enter the time duretion of movie : ")
            add_videos(name, time)

        elif choice == '3':
            video_id = input("Enter the video id to update : ")
            name = input("Enter the movie name : ")
            time = input("Enter the time duretion of movie : ")
            update_videos(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter the video id to delete : ")
            delete_videos(video_id)

        elif choice == '5':
            break

        else:
            print("Invalid Syntax.")

    conn.close()

if __name__ == "__main__":
    main()