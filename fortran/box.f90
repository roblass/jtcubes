!The purpose of this program is to create a box of points
! and find the first nearest neighbors of each point. 
program box_of_points
implicit none
integer i,j,k,cnt,totneighs
integer xmax, ymax, zmax, pmax
integer numneigh(200000), nn(100000,20)
real*8 crd(200000,3)
real*8 rsq, dx, dy, dz, cut, cutsq

!side lengths of the box
xmax = 50
ymax = 50 
zmax = 50
!total number of points
pmax = xmax*ymax*zmax
!radius of the cutoff for nearest neighbor
cut = 1.5 
cutsq = cut*cut
!initialize counters
cnt = 0 
totneighs = 0

! create the box
do i = 1, xmax
   do j = 1, ymax
      do k = 1, zmax
         cnt = cnt + 1
         crd(cnt,1) = 1.0*i
         crd(cnt,2) = 1.0*j
         crd(cnt,3) = 1.0*k
      enddo
   enddo
enddo

! find the neighbors
do i = 1, pmax
   numneigh(i) = 0
   do j = 1, pmax
      if (j.eq.i) cycle
      dx = crd(j,1)-crd(i,1)
      dy = crd(j,2)-crd(i,2)
      dz = crd(j,3)-crd(i,3)
      rsq = dx*dx + dy*dy + dz*dz
      if (rsq.lt.cutsq) then
         numneigh(i) = numneigh(i) + 1
         nn(i,numneigh(i)) = j
      endif
   enddo
   totneighs = totneighs + numneigh(i)
enddo

write(*,*) 'The number of first neighbors is ',totneighs
write(*,*) 'The dimensions of the box are ', xmax, ymax, zmax
write(*,*) 'The total number of points is ', pmax

end 
