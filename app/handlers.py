from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.generators import ai_generate

router = Router()

class Generate(StatesGroup):
    wait = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(f'Hi, would you like to ask a question?')
    await state.clear()

@router.message(Command('ask'))
async def get_msg(message: Message):
    await message.answer('good')

@router.message(Generate.wait)
async def generate_error(message: Message):
    await message.answer('Wait, its generating')

@router.message()
async def generate(message: Message, state: FSMContext):
    await state.set_state(Generate.wait)
    response = await ai_generate(message.text)
    await message.answer(response)
    await state.clear()