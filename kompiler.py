B
    �S\4  �               @   s�   d dl Z d dlZd dlZdZdd� Zdd� Ze�d� ee� ed� ed	� ed
�Z	e	dkrfe�  ne	dkrve�  ned� dS )�    Nz�[1;36m
     _  _
   _| || |_          [1;32mCOMPILER PYTHON[1;36m
  |_  ..  _|
  |_      _| [1;31mContact=>https://t.me/kang_nuubi[1;36m
    |_||_|   [1;31mGithub=>https://github.com/KANG-NEWBIE
c              C   s�   y�t �d� tt� td�} t| ��� }t|dd�}t�	|�}td|  d�}|�
d� |�
dt|� d	 � |��  t�d
� td|  � t�  W n   td� t�  Y nX d S )N�clearz#[1;37mMasukan Nama File => [1;32m� �exec�Hasil_�wzimport marshal
zexec(marshal.loads(z))g      �?z.[1;32mFile Berhasil Tercompile: [1;36mHasil_z}
[1;31m[!] ERROR: PASTIKAN FILE YANG MAU DI COMPILE BERADA DI FOLDER YANG SAMA DAN PASTIKAN ANDA MENGINPUT FILE DENGAN BENAR)�os�system�print�banner�input�open�read�compile�marshal�dumps�write�repr�close�time�sleep�exit)�a�x�b�c�d� r   �kompiler.py�py
   s"    




r   c              C   s�   y�t �d� tt� td�} t| ��� }t|dd�}t�	|�}td|  d�}|�
d� |�
dt|� d	 � |��  t�d
� td|  � t W n   td� t�  Y nX d S )Nr   z#[1;37mMasukan Nama File => [1;32mr   r   r   r   zimport marshal
zexec(marshal.loads(z))g      �?z.[1;32mFile Berhasil Tercompile: [1;36mHasil_z}
[1;31m[!] ERROR: PASTIKAN FILE YANG MAU DI COMPILE BERADA DI FOLDER YANG SAMA DAN PASTIKAN ANDA MENGINPUT FILE DENGAN BENAR)r   r   r	   r
   Z	raw_inputr   r   r   r   r   r   r   r   r   r   r   )r   r   r   r   r   r   r   r   �py2   s"    



r   r   z[1;32m[1] Python3z[2] Python2z/[1;37m[?] MAU COMPILE PYTHON BERAPA => [1;32m�1�   z
[1;31m[!] PILIHANMU SALAH)
r   r   r   r
   r   r   r   r	   r   �askr   r   r   r   �<module>   s   
