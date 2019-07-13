#include <iostream>
#include <vector>
#include <climits>
#include <queue>
#include <fstream>
using namespace std;

class Edge
{
public:
    int successor;
    int weight;
    Edge(int x = -1, int weight = INT_MAX){
        this -> successor = x ;
        this -> weight = weight;
    }
    bool operator > (const Edge &e) const
    {
        return (weight > e.weight);
    }
};

int main()
{
    ifstream in ("data.txt");
    vector<vector<Edge> > graph;
    int vertices,start,a,b,c;

    in>> vertices; // number of verticies
    in>> start;    // start of paths

    int distance [vertices];
    bool check [vertices];
    graph.resize(vertices);
    for (int i=0;i<vertices;i++)
    {
        check[i]=0;
        distance[i]=INT_MAX;
    }

    while (in>> a>>b>>c) // undirected edge between a and b with value c
    {
        graph[a].push_back(Edge(b,c));
                                       //   if you want to use that program for directed graph
        graph[b].push_back(Edge(a,c)); //<- you must comment/delete that line
    }
    priority_queue<vector <Edge>, vector <Edge>, greater<Edge> > queuePrio;
    distance[start]=0;
    queuePrio.push(Edge(start,0));
    int x;
    while(!queuePrio.empty())
    {
    	while(true)
    	{
    	if(queuePrio.empty())
            break;

    	 x=queuePrio.top().successor;

    	 if(check[x]==1)
            queuePrio.pop();
    	 else
            break;
    	}
      if(queuePrio.empty())
    	break;

    queuePrio.pop();
    check[x]=1;

      for(int i=0;i<graph[x].size();i++)
      {
          if(distance[graph[x][i].successor]> (distance[x]+ graph[x][i].weight))
          {
             distance[graph[x][i].successor]=distance[x]+graph[x][i].weight;
             queuePrio.push(Edge(graph[x][i].successor, distance[graph[x][i].successor]));
          }
      }
    }

    cout << "The shortest path from " << start<<endl;
    for (int i=0;i<vertices;i++)
    {
        cout << "to " << i<< " equals "<< distance[i]<<endl;
    }
    return 0;
}
