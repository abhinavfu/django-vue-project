# TODO There's certainly more than one way to do this task, so take your pick.
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib import auth

from rest_framework import generics, status
from rest_framework.response import Response


# Class Based API views
"""
User : admin2
pass : 1234
"""

class PostListView(generics.ListCreateAPIView):
    """
    Clased Based Post List API view.
    
    Users can create a new Post with following fields
            'text','user'
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by('-timestamp')

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=auth.get_user(request))

            data = {}
            data['text'] = request.data["text"]
            data['user'] = user.id
            serializer = PostSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"response":serializer.data,"message":"Post created successfully."},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"response":f"ERROR - {str(e)}","message":"You are not authenticated User or ERROR"},status=status.HTTP_400_BAD_REQUEST)
 

        

class PostView(generics.RetrieveUpdateDestroyAPIView):
    """
    Clased Based Post Single item API view can retrieve single Post 
    or can update single Post or can Delete the particular Post.
    
    Retrieve details of a specific Post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self,post_id):
        return Post.objects.get(id=post_id)
    
    def get(self, request,post_id, *args, **kwargs):
        post =  Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response({"response":serializer.data})
   
    def update(self, request, post_id, *args, **kwargs):
        try:
            post = Post.objects.get(id=post_id, user = self.request.user)
            
            data = {}
            data['text'] = request.data["text"]
            serializer = PostSerializer(post, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"response":serializer.data,"message":"Updated successfully."},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"response":f"ERROR - {str(e)}","message":"You are not authenticated User or ERROR"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, post_id, *args, **kwargs):
        """
        Only Admin can delete Post's record.
        """
        try:
            if self.request.user.is_superuser:
                post = Post.objects.get(id=post_id)
                post.delete()
                return Response({"response":"","message":"Post deleted successfully."},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"response":"","message":"You are not Admin."},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"response":f"ERROR - {str(e)}","message":""},status=status.HTTP_400_BAD_REQUEST)




class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all().order_by('-timestamp') 

    def create(self, request,post_id, *args, **kwargs):
        try:
            user = User.objects.get(username=auth.get_user(request))
            post = Post.objects.get(id=post_id)

            data = {"user":user.id,"post":post.id,"text":request.POST['text']}
            serializer = CommentSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"response":serializer.data,"message":"Commented successfully."},status=status.HTTP_201_CREATED)
            else:
                return Response({"response":"","message":"You are not authenticated user."},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"response":f"{str(e)}","message":"ERROR"},status=status.HTTP_400_BAD_REQUEST)



class CommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self,comment_id):
        return Comment.objects.get(id=comment_id)
    
    def get(self, request,comment_id, *args, **kwargs):
        comment =  Comment.objects.get(id=comment_id)
        serializer = CommentSerializer(comment)
        return Response({"response":serializer.data})
    
    def update(self, request, comment_id, *args, **kwargs):
        try:
            comment = Comment.objects.get(id=comment_id)
            data = {}
            data['text'] = request.POST['text']
            serializer = CommentSerializer(comment,data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response({"response":serializer.data,"message":"Cpmment updated successfully."},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"response":f"{str(e)}","message":"ERROR"},status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request,comment_id, *args, **kwargs):
        """
        Only Admin can delete comment record.
        """
        try:
            if self.request.user.is_superuser:
                obj_PO = Comment.objects.get(id=comment_id)
                obj_PO.delete()
                
                return Response({"response":"","message":"Comment deleted successfully."},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"response":"","message":"You are not Admin."},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"response":str(e),"message":"ERROR"},status=status.HTTP_400_BAD_REQUEST)


class RandomCommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    
    def get(self, request, post_id, *args, **kwargs):
        post = Post.objects.get(id=post_id)
        comments_list =  Comment.objects.filter(post=post.id)

        # random comments
        import random
        total_random_comments = 3 # random comments count
        if len(comments_list) > total_random_comments:
            comments = set()
            while len(comments)<total_random_comments:
                    items = random.choices(comments_list, k=1) # [one_item]
                    comments.add(*items)
            
            serializer = CommentSerializer(comments, many=True)
            return Response({"response":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"response":f"To get random comments in a post, there should be atleast {total_random_comments+1} comments on a post"}, status=status.HTTP_200_OK)
