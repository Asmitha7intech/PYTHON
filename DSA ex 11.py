class SocialMediaPostManagement:
    def __init__(self):
        # List to store posts as tuples
        self.posts = []

    def add_post(self):
        # Create a new post
        content = input("Enter post content: ")
        author = input("Enter your name: ")
        post = (content, author, [])  # Tuple: (content, author, comments list)
        self.posts.append(post)
        print(f"Post added by {author}.")

    def add_comment(self):
        # Add a comment to a specific post
        post_index = int(input(f"Enter the post number to comment on (1 to {len(self.posts)}): ")) - 1
        
        if 0 <= post_index < len(self.posts):
            comment = input("Enter your comment: ")
            # Add comment to the selected post
            post_content, author, comments = self.posts[post_index]
            comments.append(comment)
            print(f"Comment added to the post by {author}.")
        else:
            print("Invalid post number.")

    def display_posts(self):
        # Display all posts and their comments
        if not self.posts:
            print("No posts available.")
            return
        
        for index in range(len(self.posts)):
            post_content, author, comments = self.posts[index]
            print(f"Post {index + 1}: {post_content} (by {author})")
            if comments:
                print("Comments:")
                for comment in comments:
                    print(f"- {comment}")
            else:
                print("No comments yet.")
            print(f"Total comments: {len(comments)}\n")

    def generate_post_summary(self):
        # Generate a summary of each post
        if not self.posts:
            print("No posts available.")
            return
        
        for index in range(len(self.posts)):
            post_content, author, comments = self.posts[index]
            print(f"Post {index + 1} summary:")
            print(f"Post: {post_content} (by {author})")
            print(f"Total comments: {len(comments)}\n")


# Example usage
def main():
    smm_system = SocialMediaPostManagement()

    while True:
        print("\n--- Social Media Post Management ---")
        print("1. Add Post")
        print("2. Add Comment")
        print("3. Display Posts")
        print("4. Generate Post Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            smm_system.add_post()
        elif choice == '2':
            smm_system.add_comment()
        elif choice == '3':
            smm_system.display_posts()
        elif choice == '4':
            smm_system.generate_post_summary()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
