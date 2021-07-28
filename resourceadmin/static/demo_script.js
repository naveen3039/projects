function yesnoCheck(that) 
{
    if (that.value == "True") 
    {
        document.getElementById("ils").style.display = "block";
        document.getElementById("pim").style.display = "block";
        document.getElementById("iei").style.display = "block";
        document.getElementById("imi").style.display = "block";
        document.getElementById("im").style.display = "block";
    }
    else
    {
        document.getElementById("ils").style.display = "none";
        document.getElementById("pim").style.display = "none";
        document.getElementById("iei").style.display = "none";
        document.getElementById("imi").style.display = "none";
        document.getElementById("im").style.display = "none";
    }
}