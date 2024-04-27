graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['A', 'C']
}



```mermaid  
graph TD;  
A-->B; A-->C;
B-->C; B-->D;
C-->E;
D-->A; D-->C
```