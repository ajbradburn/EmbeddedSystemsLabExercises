.data
.balign 4
numbers: .word 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

.text
.balign 4
.global main
.func main

main:
  mov r0, #5
  mov r1, #5
    /* r0 + 5 */
  add r0, r0, r1

  ldr r2, numbers_address
  ldr r1, [r2], #4
    /* r0 + 10 */
  sub r0, r0, r1
  ldr r1, [r2], #4
    /* r0 + 9 */
  sub r0, r0, r1
  ldr r1, [r2], #4
    /* r0 + 8 */
  sub r0, r0, r1
  ldr r1, [r2], #4
    /* r0 + 7 */
  sub r0, r0, r1
  ldr r1, [r2], #4
    /* r0 + 6 */
  sub r0, r0, r1
  ldr r1, [r2], #4
    /* r0 + 5 */
  sub r0, r0, r1
  ldr r1, [r2], #4
    /* r0 + 4 */
  sub r0, r0, r1
  ldr r1, [r2], #4
    /* r0 + 3 */
  sub r0, r0, r1
  ldr r1, [r2], #4
    /* r0 + 2 */
  sub r0, r0, r1
  ldr r1, [r2], #4
    /* r0 + 1 */
  sub r0, r0, r1

    /* Clear register 0 */
  eor r0, r0, r0

  bx lr

numbers_address: .word numbers
