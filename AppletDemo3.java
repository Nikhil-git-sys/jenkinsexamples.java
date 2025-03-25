import java.applet.*;
import java.awt.*;
/*<applet code="AppletDemo3.class" width="300" height="300">
</applet>*/
public class AppletDemo3 extends Applet
{
public void paint(Graphics g)
{
g.setColor(Color.RED);
int x[]={200,300,300,200,100,100};
int y[]={0,100,500,700,500,100};
g.fillPolygon(x,y,6);
g.drawArc(100,120,130,140,150,160);
}
}
