from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.generators import gpt4

router = Router()

class Generate(StatesGroup):
    text = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(f'Hi, would you like to ask a question?')
    await state.clear()

@router.message(Command('ask'))
async def get_msg(message: Message):
    await message.answer('good')

@router.message(F.text)
async def generate(message: Message, state: FSMContext):
    await state.set_state(Generate.text)
    response = await gpt4(message.text)
    await message.answer(response.choices[0].message.content)

@router.message(Generate.text)
async def generate_error(message: Message):
    await message.answer('Wait, its generating')