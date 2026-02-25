function addtocart(pid){
   $.get('/addtocart', {pid: pid}, function(rt){

      if (rt == 'AnonymousUser'){
         window.location.href = "/user-login"
      }
      else{
         alert(rt)
      }

   })
}