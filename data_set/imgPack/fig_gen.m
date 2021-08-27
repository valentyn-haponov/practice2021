clear all
close all

fig = figure('Renderer', 'painters', 'Position', [200 200 10 90]);
set(gca,'XTick',[], 'YTick', [])
set(gca,'visible','off')
box off
data = zeros(10,8);
for i = 1:500
%     rand
% a = 1;
% b = 1.2;
% m = 1;
% th = pi/2;
a = 1;
b = 1.1 + 1.4*rand;
m = 1 + 2*rand;
th = 0 + pi/2 * rand;

l = 300;

s = 0 : (pi^(1/a))/l : (pi^(1/a));
t = 0 : (pi^(1/b))/l : (pi^(1/b));
x = m*(cos(th).*sin(s.^a) - sin(th).*sin(t.^b));
y = m*(sin(th).*sin(s.^a) + cos(th).*sin(t.^b));
data(i,1) = i;
data(i,2) = b;
data(i,3) = m;
data(i,4) = th;

m1 = m + m*(-0.1+0.2*rand);
th1 = th + th*(-0.1+0.2*rand);
b1 = b + b*(-0.1+0.2*rand);
s1 = 0 : (pi^(1/a))/l : (pi^(1/a));
t1 = 0 : (pi^(1/b1))/l : (pi^(1/b1));
x1 = m1*(cos(th1).*sin(s1.^a) - sin(th1).*sin(t1.^b1));
y1 = m1*(sin(th1).*sin(s1.^a) + cos(th1).*sin(t1.^b1));

data(i,5) = b1;
data(i,6) = m1;
data(i,7) = th1;
data(i,8) = 0;
xx = [x -x1];
yy = [y -y1];


plot(xx,yy)
set(gca,'XTick',[], 'YTick', [])
set(gca,'visible','off')
box off
saveas(fig,sprintf('fig%d.bmp',i),'bmpmono');
end
fileID = fopen('data_res.txt','w');
fprintf(fileID,'%3.0f %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f %1.0f\r\n',data.');
fclose(fileID);

