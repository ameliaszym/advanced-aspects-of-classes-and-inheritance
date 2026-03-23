from models.tasks.comment import Comment

class CommentService:
    def add_comment(self, task, content):
        task.add_comment(Comment(content))