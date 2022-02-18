.data
.balign 4
numbers: .word 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0

.text
.balign 4
.global main
.func main

main:
  mov r0, #5
  mov r1, #5
    /* r0 + 5 */
  add r0, r0, r1

  ldr r2, =numbers
add_more:
  ldr r1, [r2], #4
    /* Is the new number equal to 0? */
  cmp r1, #0
  beq end
    /* Add new number. */
  add r0, r0, r1
    /* Do it again. */
  b add_more
end:

  bx lr
