.data
.balign 4
numbers: .word 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
.balign 4
number_count: .word 10

.text
.balign 4
.global main
.func main

main:
  mov r0, #5
  mov r1, #5
    /* r0 + 5 */
  add r0, r0, r1

    /* Create an itteration counter that starts with the number count */
  ldr r3, =number_count
  ldr r3, [r3]

  ldr r2, =numbers
add_more:
  ldr r1, [r2], #4
  add r0, r0, r1
    /* Decriment our itteration counter. */
  sub r3, r3, #1
    /* Is our itteration counter equal to 0? */
  cmp r3, #0
    /* If yes/true, jump to the end of the program. */
  beq end

    /* If no/false, do it again. */
  b add_more
end:

  bx lr
