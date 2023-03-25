import asyncio


# Coroutines are computer program cmponents that generalize subroutines for non-preemptive multitasking, by allowing execution to be suspended and resumed
# async event-loop: In computer-science, the event loop is a programming construct or design pattern that waits for and dispatches events or messages in a program


async def main():
    print("tim")
    task = asyncio.create_task(foo("text"))
    await asyncio.sleep(2)
    print("finished main")


async def foo(text):
    print(text)
    await asyncio.sleep(5)
    print("finished foo")


# asyncio creates an events loop and add the coroutine to it
asyncio.run(main())
