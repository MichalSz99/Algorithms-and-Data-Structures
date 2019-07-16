#include <iostream>
#include <vector>
#include <climits>
#include <queue>
#include <fstream>
using namespace std;

class Edge
{
private:
    friend class Graph;
    int successor;
    int weight;

    Edge(int x, int w){
       successor = x ;
       weight = w;
    }

public:
    bool operator > (const Edge &e) const
    {
        return (weight > e.weight);
    }
};

class Graph
{

private:
    int vertex;
    vector<vector<Edge> > graph;

public:
    Graph(int v){
        vertex = v;
        graph.resize(vertex);
    }

    void addEdge(int vertexA, int vertexB, int value){
        graph[vertexA].push_back(Edge(vertexB,value));  //  if you want to use that program for directed graph
        graph[vertexB].push_back(Edge(vertexA,value)); //<- you must comment/delete that line
    }

    void Dijkstra(int start){
        int distance [vertex];
        bool check [vertex];
        for (int i=0;i<vertex;i++)
        {
            check[i]= false;
            distance[i]=INT_MAX;
        }
        distance[start]=0;
        priority_queue<vector <Edge>, vector <Edge>, greater<> > queuePrio;
        queuePrio.push(Edge(start,0));
        int currentVertex;
        while(!queuePrio.empty())
        {
            while(true)
            {
                if(queuePrio.empty())
                    break;

                currentVertex =  queuePrio.top().successor;

                if(check[currentVertex]==1)
                    queuePrio.pop();
                else
                    break;
            }
            if(queuePrio.empty())
                break;

            queuePrio.pop();
            check[currentVertex] = true;

            for(int i=0; i<graph[currentVertex].size(); i++)
            {
               int currentSuccessor = graph[currentVertex][i].successor;
               int currentDistance = distance[graph[currentVertex][i].successor];
               int newDistance = distance[currentVertex]+ graph[currentVertex][i].weight;
                if( newDistance < currentDistance)
                {
                    distance[currentSuccessor] = newDistance;
                    queuePrio.push(Edge(currentSuccessor, newDistance));
                }
            }
        }

        cout << "The shortest path from " << start<<endl;
        for (int i=0;i<vertex;i++)
        {
            cout << "to " << i<< " equals "<< distance[i]<<endl;
        }
    }

};

int main()
{
    ifstream in ("dataDijkstra.txt");
    int v,start,vA,vB,val;
    in >> v; // number of verticies
    in >> start;    // start of paths
    Graph graph= Graph(v);
    while (in>> vA >> vB >> val) // edge between a and b with value c
    {
        graph.addEdge(vA,vB, val);
    }
    graph.Dijkstra(0);
    return 0;
}
