function [a]=Hamdistance(f,fd)
a=fscanf(f,'%s');
m=a;
fprintf(fd,'%s\r\n',m);
c=a(1);
fclose(f);
b=length(a);
for i=1:b
    c=a(i);
    switch c=='A'
       case 1
          a(i)='T';
          a1=a;
          fprintf(fd,'%s\r\n',a1);
          a(i)='C';
          a2=a;
          fprintf(fd,'%s\r\n',a2);
          a(i)='G';
          a3=a; 
          fprintf(fd,'%s\r\n',a3);
    end
    switch c=='T'
       case 1
          a(i:i)='A';
          a1=a;
          fprintf(fd,'%s\r\n',a1);
          a(i:i)='C';
          a2=a;
          fprintf(fd,'%s\r\n',a2);
          a(i:i)='G';
          a3=a; 
          fprintf(fd,'%s\r\n',a3);
          
    end
    switch c=='C'
       case 1
          a(i:i)='T';
          a1=a;
          fprintf(fd,'%s\r\n',a1);
          a(i:i)='A';
          a2=a;
          fprintf(fd,'%s\r\n',a2);
          a(i:i)='G';
          a3=a; 
          fprintf(fd,'%s\r\n',a3);
    end
    switch c=='G'
       case 1
          a(i:i)='T';
          a1=a;
          fprintf(fd,'%s\r\n',a1);
          a(i:i)='C';
          a2=a;
          fprintf(fd,'%s\r\n',a2);
          a(i:i)='A';
          a3=a; 
          fprintf(fd,'%s\r\n',a3);
    end
   a=m;
end

a=m;
for i=1:b
    c1=a(i:i);
    for j=(i+1):b
        switch c1=='A'
            case 1
            a(i:i)='C';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a;
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
         end
         switch c1=='A'
            case 1
            a(i:i)='G';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
         end
         switch c1=='A'
            case 1
            a(i:i)='T';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
        end
        switch c1=='C'
            case 1
            a(i:i)='A';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
        end 
        switch c1=='C'
            case 1
            a(i:i)='G';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a;
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
        end
        switch c1=='C'
            case 1
            a(i:i)='T';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
        end
        switch c1=='T'
            case 1
            a(i:i)='C';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a;
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
         end
          switch c1=='T'
             case 1
             a(i:i)='G';
             switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
             end
             switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
         end
         switch c1=='T'
             case 1
             a(i:i)='A';
             switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
        end
        switch c1=='G'
            case 1
            a(i:i)='C';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a;
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
        end 
        switch c1=='G'
            case 1
            a(i:i)='A';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
        end
        switch c1=='G'
            case 1
            a(i:i)='T';
            switch a(j:j)=='A'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='A';
            end
            switch a(j:j)=='T'
                case 1
                a(j:j)='A';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='T';
             end
             switch a(j:j)=='C'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='A';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='G';
                a3=a; 
                fprintf(fd,'%s\r\n',a3);
                a(j:j)='C';
             end
             switch a(j:j)=='G'
                case 1
                a(j:j)='T';
                a1=a;
                fprintf(fd,'%s\r\n',a1);
                a(j:j)='C';
                a2=a;
                fprintf(fd,'%s\r\n',a2);
                a(j:j)='A';
                a3=a; 
                fprintf(fd,'%s\r\n',a3); 
                a(j:j)='G';
             end
        end
    end
    a=m;
end