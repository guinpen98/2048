import numpy as np
class Game:
    def init(self):
        self.start()

    def start(self):
        self.board = np.zeros([4,4]) # �Ֆʂ̏�����
        self.score = 0 # �X�R�A�̏�����
        x = np.random.randint(0,4) 
        y = np.random.randint(0,4)
        # �ՖʂɃ����_����2�𐶐�
        self.board[y][x] = 2 
        while(True):
            x = np.random.randint(0,4) 
            y = np.random.randint(0,4)
            if self.board[y][x]==0:
                self.board[y][x] = 2
                break
    
    def action(self,action_select):
        reward = 0 # ��V�̏�����

        if action_select==0: # ���ɃX���C�v
            for y in range(4):
                z_cnt = 0 # �l��0�ł���}�X�̐�
                prev = -1 # 0�𔲂��������ׂ̃}�X�̒l
                for x in range(4):
                    if self.board[y][x]==0: # �l��0�̎�
                        z_cnt += 1
                    elif self.board[y][x]==prev: # ���ׂ̃}�X�ƒl��������
                        z_cnt += 1
                        self.board[y][x-z_cnt] *= 2 # ���ׂɂ���}�X�̒l���{�ɂ���
                        self.board[y][x] = 0
                        reward += self.board[y][x-z_cnt]
                        self.score += self.board[y][x-z_cnt]
                        prev = -1
                    else:
                        prev = self.board[y][x]
                        if z_cnt==0: # �l��0�ł���}�X�̕��A�l���ړ�������
                            continue
                        self.board[y][x] = 0
                        self.board[y][x-z_cnt] = prev
                        
        elif action_select==1: # �E�ɃX���C�v
            for y in range(4):
                z_cnt = 0 # �l��0�ł���}�X�̐�
                prev = -1 # 0�𔲂������E�ׂ̃}�X�̒l
                for x in range(4):
                    if self.board[y][3-x]==0: # �l��0�̎�
                        z_cnt += 1
                    elif self.board[y][x]==prev: # �E�ׂ̃}�X�ƒl��������
                        z_cnt += 1
                        self.board[y][3-x+z_cnt] *= 2 # �E�ׂɂ���}�X�̒l���{�ɂ���
                        self.board[y][3-x] = 0
                        reward += self.board[y][3-x+z_cnt]
                        self.score += self.board[y][3-x+z_cnt]
                        prev = -1
                    else:
                        prev = self.board[y][3-x]
                        if z_cnt==0: # �l��0�ł���}�X�̕��A�l���ړ�������
                            continue
                        self.board[y][3-x] = 0
                        self.board[y][3-x+z_cnt] = prev

        elif action_select==2: # ��ɃX���C�v
            for x in range(4):
                z_cnt = 0 # �l��0�ł���}�X�̐�
                prev = -1 # 0�𔲂�������ׂ̃}�X�̒l
                for y in range(4):
                    if self.board[y][x]==0: # �l��0�̎�
                        z_cnt += 1
                    elif self.board[y][x]==prev: # ��ׂ̃}�X�ƒl��������
                        z_cnt += 1
                        self.board[y-z_cnt][x] *= 2 # ��ׂɂ���}�X�̒l���{�ɂ���
                        self.board[y][x] = 0
                        reward += self.board[y-z_cnt][x]
                        self.score += self.board[y-z_cnt][x]
                        prev = -1
                    else:
                        prev = self.board[y][x]
                        if z_cnt==0: # �l��0�ł���}�X�̕��A�l���ړ�������
                            continue
                        self.board[y][x] = 0
                        self.board[y-z_cnt][x] = prev
                        
        elif action_select==3: # ���ɃX���C�v
            for x in range(4):
                z_cnt = 0 # �l��0�ł���}�X�̐�
                prev = -1 # 0�𔲂��������ׂ̃}�X�̒l
                for y in range(4):
                    if self.board[3-y][x]==0: # �l��0�̎�
                        z_cnt += 1
                    elif self.board[y][x]==prev: # ���ׂ̃}�X�ƒl��������
                        z_cnt += 1
                        self.board[3-y+z_cnt][x] *= 2 # ���ׂɂ���}�X�̒l���{�ɂ���
                        self.board[3-y][x] = 0
                        reward += self.board[3-y+z_cnt][x]
                        self.score += self.board[3-y+z_cnt][x]
                        prev = -1
                    else:
                        prev = self.board[3-y][x]
                        if z_cnt==0: # �l��0�ł���}�X�̕��A�l���ړ�������
                            continue
                        self.board[3-y][x] = 0
                        self.board[3-y+z_cnt][x] = prev

        while(True):
            y = np.random.randint(0,4)
            x = np.random.randint(0,4)
            if self.board[y][x]==0:
                if np.random.random() < 0.2: # 20%�̊m����4�����������
                    self.board[y][x] = 4
                else:
                    self.board[y][x] = 2
                break

        return reward




