
A=input("ENTER IMAGE NAME: ","s");
B=input("ENTER IMAGE NAME: ","s");
im1=imread(A);
im2=imread(B);
diff_hist=imhist(im1)-imhist(im2);
plot(diff_hist);
disp(diff_hist);

if diff_hist==0
    disp("YES THEY BOTH ARE REAL IMAGE");
else
    disp("NO");
end
    
