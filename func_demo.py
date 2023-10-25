{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3c2c32ab-0718-424d-8876-f4feceacdeac",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_even(number):\n",
    "    if number%2 == 0:\n",
    "        return \"Even\"\n",
    "    else:\n",
    "        return \"Odd\"\n",
    "   \n",
    "      \n",
    "    \n",
    "    \"\"\"\n",
    "    This function tells if a given number is odd or even \n",
    "    input - any valid integer \n",
    "    output- odd/even \n",
    "    created by - Saurabh\n",
    "    Last edited - 03 Sept 2023\n",
    "    \"\"\"\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ae18f76d-20e4-4eb5-8208-aa8868162650",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Odd\n",
      "Even\n",
      "Odd\n",
      "Even\n",
      "Odd\n",
      "Even\n",
      "Odd\n",
      "Even\n",
      "Odd\n",
      "Even\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,11):\n",
    "    print(is_even(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "96a1e2f6-a4ee-415a-a3bc-0a942b1ed304",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(is_even.__doc__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7437659f-eaf9-404a-b8b5-4c50c1bcc6f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"type(object) -> the object's type\\ntype(name, bases, dict, **kwds) -> a new type\""
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type.__doc__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92cd3e9f-56e9-4b2b-9f28-046b33f524b0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
