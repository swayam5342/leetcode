# Last updated: 9/1/2026, 7:54:45 PM
1from collections import deque
2from typing import List
3
4class Solution:
5    def minMoves(self, classroom: List[str], energy: int) -> int:
6        m, n = len(classroom), len(classroom[0])
7        start = None
8        litter_positions = []
9        
10        for i in range(m):
11            for j in range(n):
12                if classroom[i][j] == 'S':
13                    start = (i, j)
14                elif classroom[i][j] == 'L':
15                    litter_positions.append((i, j))
16        
17        if not start:
18            return -1
19        
20        num_litter = len(litter_positions)
21        if num_litter == 0:
22            return 0
23        
24        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
25
26        visited = {}
27        
28        initial_mask = 0
29        for idx, pos in enumerate(litter_positions):
30            if pos == start:
31                initial_mask |= (1 << idx)
32                break
33        
34        queue = deque([(start[0], start[1], energy, initial_mask, 0)])
35        visited[(start[0], start[1], initial_mask)] = energy
36        
37        while queue:
38            row, col, curr_energy, mask, moves = queue.popleft()
39            
40            if mask == (1 << num_litter) - 1:
41                return moves
42
43            key = (row, col, mask)
44            if curr_energy < visited.get(key, -1):
45                continue
46            if curr_energy == 0 and classroom[row][col] != 'R':
47                continue
48            
49            for dr, dc in directions:
50                nr, nc = row + dr, col + dc
51                
52                if not (0 <= nr < m and 0 <= nc < n):
53                    continue
54                if classroom[nr][nc] == 'X':
55                    continue
56                
57                new_energy = curr_energy - 1
58                if new_energy < 0:
59                    continue
60                
61                new_mask = mask
62                if classroom[nr][nc] == 'L':
63                    for idx, pos in enumerate(litter_positions):
64                        if pos == (nr, nc):
65                            new_mask |= (1 << idx)
66                            break
67                
68                if classroom[nr][nc] == 'R':
69                    new_energy = energy
70                
71                new_key = (nr, nc, new_mask)
72                if new_energy > visited.get(new_key, -1):
73                    visited[new_key] = new_energy
74                    queue.append((nr, nc, new_energy, new_mask, moves + 1))
75        
76        return -1