
    function Details()
    {
        var name = document.getElementById("name").value;          
        var about = document.getElementById("about").value;        
        var phoneno = document.getElementById("phoneno.").value;
        var address = document.getElementById("address").value;
        var college = document.getElementById("college").value;

        var fname = name;
        document.getElementById("span1").textContent = fname;
        var fabout = about;
        document.getElementById("span2").textContent = fabout;
        var fphoneno = phoneno; 
        document.getElementById("span3").textContent = fphoneno;
        var faddress = address;
        document.getElementById("span4").textContent = faddress;
        var fcollege = college;
        document.getElementById("span5").textContent = fcollege;
        
    }