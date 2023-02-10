
urlpatterns=[
path('Add', views.Add, name='Category_Add'),
    path('Update/<int:catid>', views.Update, name='Category_Update'),

]