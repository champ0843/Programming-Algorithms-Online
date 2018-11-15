#include <stdio.h>

int main(void) {
	int result;
	int T,n;
	double detail[3];
	double sum=0,loss,profit;
	scanf("%d",&T);
	while(T--)
	{
	    scanf("%d",&n);
	    sum=0;
	    while(n--)
	    {
	        for(int i=0;i<3;i++)
	        {
	            scanf("%lf",&detail[i]);
	        }
	        profit=detail[0]+(detail[2]*detail[0])/100;
	        loss=profit-(detail[2]*profit)/100;
	        sum=sum+detail[1]*(detail[0]-loss);
	       // printf("%lf\n%lf\n%lf\n",profit,loss,sum);
	        
	    }
	    printf("%lf\n",sum);
	}
	
	return 0;
}

