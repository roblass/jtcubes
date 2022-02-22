#!The purpose of this program is to create a box of points
#! and find the first nearest neighbors of each point. 
#program box_of_points
#implicit none
#integer i,j,k,cnt,totneighs
#integer xmax, ymax, zmax, pmax
#integer numneigh(100000), nn(100000,20)
#real*8 crd(100000,3)
#real*8 rsq, dx, dy, dz, cut, cutsq
import sys

#!side lengths of the box
#xmax = 30
#ymax = 30
#zmax = 30

xmax, ymax, zmax = [int(x) for x in sys.argv[1:]]
crd = {}

#!total number of points
#pmax = xmax*ymax*zmax
pmax = xmax * ymax * zmax

#!radius of the cutoff for nearest neighbor
#cut = 1.5 
cut = 1.5

#cutsq = cut*cut
cutsq = cut*cut

#!initialize counters
#cnt = 0 
#totneighs = 0
cnt = 0
totneighs = 0

#! create the box
#do i = 1, xmax
   #do j = 1, ymax
      #do k = 1, zmax
         #cnt = cnt + 1
         #crd(cnt,1) = 1.0*i
         #crd(cnt,2) = 1.0*j
         #crd(cnt,3) = 1.0*k
      #enddo
   #enddo
#enddo

for i in range(1, xmax + 1):
    for j in range(1, ymax + 1):
        for k in range(1, zmax + 1):
            cnt += 1
            crd[(cnt, 1)] = 1.0 * i
            crd[(cnt, 2)] = 1.0 * j
            crd[(cnt, 3)] = 1.0 * k


#! find the neighbors
#do i = 1, pmax
   #numneigh(i) = 0
   #do j = 1, pmax
      #if (j.eq.i) cycle
      #dx = crd(j,1)-crd(i,1)
      #dy = crd(j,2)-crd(i,2)
      #dz = crd(j,3)-crd(i,3)
      #rsq = dx*dx + dy*dy + dz*dz
      #if (rsq.lt.cutsq) then
         #numneigh(i) = numneigh(i) + 1
         #nn(i,numneigh(i)) = j
      #endif
   #enddo
   #totneighs = totneighs + numneigh(i)
#enddo

numneigh = {}
for i in range(1, pmax + 1):
    numneigh[i] = 0
    for j in range(1, pmax + 1):
        if j == i:
            continue
        dx = crd[(j, 1)] - crd[(i, 1)]
        dy = crd[(j, 2)] - crd[(i, 2)]
        dz = crd[(j, 3)] - crd[(i, 3)]
        rsq = dx * dx + dy * dy + dz * dz
        if rsq < cutsq:
            numneigh[i] += 1
    totneighs += numneigh[i]

#write(*,*) 'The number of first neighbors is ',totneighs
#write(*,*) 'The dimensions of the box are ', xmax, ymax, zmax
#write(*,*) 'The total number of points is ', pmax

print(f"The number of first neighbors is {totneighs}")
print(f"The dimensions of the box are {xmax}, {ymax}, {zmax}")
print(f"The total number of points is {pmax}")

#end 
