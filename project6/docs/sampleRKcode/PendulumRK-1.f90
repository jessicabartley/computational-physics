! ------------------------------------------------------------------------------

! Project 6 (driven pendulum) using SLATEC DERKF (Runge-Kutta)

  PROGRAM pendulum

! declarations
  IMPLICIT NONE
  REAL, PARAMETER :: PI=3.14159265358979
  INTEGER, PARAMETER :: NEQ=2, LRW=33+7*NEQ, LIW=34
  REAL, DIMENSION(2) :: RPAR
  INTEGER, DIMENSION(1) :: IPAR
  REAL :: T,TOUT
  REAL, DIMENSION(NEQ) :: Y
  INTEGER, DIMENSION(15) :: INFO
  REAL :: RTOL,ATOL
  REAL, DIMENSION(LRW) :: RWORK
  INTEGER, DIMENSION(LIW) :: IWORK
  INTEGER :: IDID
  EXTERNAL F
  INTEGER :: i,N
  REAL :: H

  T=0.0
  Y(1)=0.0
  Y(2)=0.1

  INFO(:)=0
  RTOL=0.01
  ATOL=1.0

  RPAR(1)=0.0
  RPAR(2)=0.1
  IPAR(1)=0

  N=1000
  H=0.01

  open(16,file='PendulumRK.out',FORM='FORMATTED',STATUS='UNKNOWN')

  i=0
  WRITE(16,'(I4,3ES14.6)') i,T,Y(1),Y(2)

  DO i=1,N
    INFO(1)=0
    TOUT=T+H
    CALL DERKF (F, NEQ, T, Y, TOUT, INFO, RTOL, ATOL, IDID, RWORK, LRW, IWORK, LIW, RPAR, IPAR)
    T=TOUT
    WRITE(16,'(I4,3ES14.6)') i,T,Y(1),Y(2)
  ENDDO

  CLOSE (16)

  END PROGRAM pendulum

! ------------------------------------------------------------------------------

  SUBROUTINE F(X,U,UPRIME,RPAR,IPAR)

  IMPLICIT NONE
  REAL, INTENT(in) :: X
  REAL, DIMENSION(*), INTENT(IN) :: U
  REAL, DIMENSION(*), INTENT(OUT) :: UPRIME
  REAL, DIMENSION(*), INTENT(IN) :: RPAR
  INTEGER, DIMENSION(*), INTENT(IN) :: IPAR

! RPAR(1) = $a$ (amplitude)
! RPAR(2) = $\omega$ (driving frequency)
! IPAR(1) = redundant (dummy)

  UPRIME(1) = U(2)
  UPRIME(2) = -SIN(U(1))+RPAR(1)*COS(RPAR(2)*X)

  END SUBROUTINE F

! ------------------------------------------------------------------------------
