import numpy as np

class CreateLabel():
    @staticmethod
    def connect_pts(pt1, pt2):
        """
        判断 pt1, pt2 是否相连, 若否, 插入点使其相连.
        注意: 由于 cv2 的坐标为(col, row), 与 array <-> img 的标识方法不同, 因此在本函数中只以 col, row 表示, 不以 x, y 表示.
        前开后闭.
        经确认上右下左四向无问题.
        :param pt1: list 上一个点 [col, row]
        :param pt2: list 新的点   [col, row]
        :return: line_list
        """
        line_list = [pt1] # 先将第一个点放入line_list
        row1, col1 = pt1
        row2, col2 = pt2
        if abs(row1 - row2) > 1:
            """
            X|O|O
            O|O|O
            O|X|O 
            """
            if row1 < row2:
                for row in range(row1 + 1, row2):  # 不填写后端点.
                    col = int((col2 - col1) / (row2 - row1) * (row - row1) + col1)
                    line_list.append([row, col])
            elif row2 < row1:
                for row in range(row1 - 1, row2, -1):
                    col = int((col2 - col1) / (row2 - row1) * (row - row1) + col1)
                    line_list.append([row, col])
            assert len(line_list) == abs(pt1[0] - pt2[0])

        else: #if row1 == row2:  # 填成直线.
            if col1 < col2:
                for col in range(col1 + 1, col2): # 不填写后端点.
                    line_list.append([row1, col])
                assert len(line_list) == abs(pt2[1] - pt1[1])
            elif col2 < col1:
                for col in range(col1 - 1, col2, -1):
                    line_list.append([row1, col])
                assert len(line_list) == abs(pt2[1] - pt1[1])
            else:
                assert len(line_list) == 1
        return line_list

    @staticmethod
    def add_dict(dict, list, idx):
        """
        将新的点 list 加入到之前的点 dict 中.
        首先: 取出当前点和下一个点.
        第二: 连接两个点.
        第三: 将新的list插入dict中.
        :param dict: {'row': [col, idx], ...}
        :param list: [[col, row], ...]
        :param idx: list 起始点在edge_list 中的位置.
        :return: dict, flag_closed: bool, 闭合与否.
        """
        assert len(list) > 0
        for i, pt in enumerate(list):
            row, col = pt
            if i == 0:
                if row in dict.keys():
                    dict[row].append([col, idx])
                else:
                    dict[row] = [[col, idx]]
            else:
                if row in dict.keys():
                    dict[row].append([col, -1])
                else:
                    dict[row] = [[col, -1]]

    @classmethod
    def labelize(cls, edge_list, edge_dict, img_shape):
        """
        如果是尖锐的角, 都需要加二.
        怎么判断是尖锐地角: 构成这个点的两条线段的斜率小于零。
        [pt[i-1], pt[i], pt[i+1]] 在row方向呈 近|远|近, 或 远|近|远 的关系.
        (pt[i-1][row] - pt[i][row]) * (pt[i+1][row] - pt[i][row]) > 0
        远近远 -> '+' * '+' -> '+'
        近远近 -> '-' * '-' -> '+'

        如果有一条边:
            (pt[i-1][row] - pt[i][row]) * (pt[i+1][row] - pt[i][row]) == 0

        edge_dict = {
            row: [[col, edge_list中的idx], [col2, edge_list中的idx], ...]
            ...
        }
        若此点并非端点, 则 idx 为 -1.

        向左做射线,
            射线与边相交: True|False 转换.
            射线与点相交:
                提取前一点, 提取后一点, 计算二者斜率乘积的正负号.
                若为正: True|False 转换.
                若为负: 不变.
            射线与边重合, 且点不在边上: True|False 转换.

        :param edge_list: 依次表现多边形的边的端点, 按顺时针录入.
        :param edge_dict: 多边形边沿上的点, index 与 value 都是sorted的状态.
        :param img_shape:
        :return:
        """
        img_label = np.zeros(tuple(img_shape))
        cls.edge_list = edge_list
        cls.edge_dict = edge_dict
        for row in edge_dict.keys():
            if len(edge_dict[row]) == 1: # 在上下出现一个角, 次点必为边界
                img_label[row, edge_dict[row][0][0]] = 2 # 将此点标上, 并移至下一行
                continue
            for col in range(edge_dict[row][0][0], edge_dict[row][-1][0] + 1):
                if cls.on_polygon([row, col]):
                    img_label[row, col] = 2
                elif cls.in_polygon(img_label, [row, col]):
                    img_label[row, col] = 1
        return  img_label # np.transpose(img_label, [1,0])

    @classmethod
    def on_polygon(cls, position):
        row, col = position
        cols = cls.edge_dict[row]
        for col_edge, _ in cols:
            if col_edge == col:
                return True
        return False

    @classmethod
    def in_polygon(cls, img_label, position):
        """
        判断 待定点前的一个拐角是否是需要变化的拐角, 随后再与待定点拐角前的角进行比较.
        需要记录四个点:
            1. nearest_edge: col 值,
                记录离的最近的边界点.
            ------------------------
            2. nearest_turning: edge_list index,
                记录离的最近的 edge_list 上的点, 用来查找下一个 edge_list 上的点是向上还是向下.
            ------------------------
            3. next_row: row 值,
                记录离的最近的 edge_list 上下一个边界点的值, 用来判断右侧走向.
            ------------------------
            4. farthest_edge: col 值,
                记录离的最远的边界点;
            ------------------------
            5. farthest_turning: edge_list index,
                记录离的最远的 edge_list 上的点, 用来查找上一个 edge_list 上的点是向上还是向下.
            ------------------------
            6. previous_row: row 值
                记录离的最远的 edge_list 的上一个边界点的值, 用来判断左侧走向.
            ------------------------
        """
        row, col = position
        cols = cls.edge_dict[row]
        nearest_turning = -1
        nearest_turning_col = -1
        nearest_edge = -1
        farthest_turning = -1
        farthest_edge = -1
        previous_row = -1
        next_row = -1
        for order, [col_edge, idx] in enumerate(cols):
            if col_edge > col:
                break  # 得到 nearest_turning 为离position最近的拐角.
            if idx > -1:  # 记录拐角
                nearest_turning = idx
        nearest_edge = cols[order - 1][0] # 得到 nearest_edge 为离 position 最近的边的 col 值.

        # 沿着 cols 向前找寻连着的点, 直到断开, 以获得 farthest_edge 和 farthest_turning
        order = order - 1
        while order >= 0:
            col_edge, idx = cols[order]
            if idx > -1:  # 记录拐角.
                farthest_turning = idx
            if order > 0:
                if abs(cols[order][0] - cols[order - 1][0]) > 1:
                    # 比较当前点与前一个点的位置关系, 若与前一个点断开, 则认为当前点是左端点
                    break  # 得到
            elif order == 0:
                # 此点定位左端点.
                break
            else:
                print('order 只可能 >=0.')
                raise ValueError
            order -= 1
        farthest_edge = cols[order][0] # 得到 farthest_edge 为离 position 最远的边的 col 值.

        if nearest_edge == -1: # position 在图形的左侧
            cnt = 0
            return cnt == 1
        if nearest_edge == farthest_edge: # 交点只有一个点, 分两种情况: V || /
            # 情况一:
            # nearest_edge == nearest_turning == farthest_turning == farthest_edge
            # 情况二:
            # nearest_edge != nearest_turning 则会导致 nearest_turning < nearest_edge = farthest_edge
            # 寻求 farthest_turning 的过程中向前遍历, 亦无解, 因此farthest_turning 为 -1
            if nearest_turning != -1:
                nearest_turning_col = cls.edge_list[nearest_turning][1]

            try:
                assert nearest_turning_col <= nearest_edge
            except AssertionError:
                print('确认nearest_turning_col 与 nearest_edge')
                print(nearest_turning_col, nearest_turning, nearest_edge, position, cols)
                raise AssertionError
            if nearest_turning_col == nearest_edge: # 四个值相等
                # 判断是 V 还是 /.
                previous_row = cls.edge_list[(farthest_turning - 1)  % len(cls.edge_list)][0]
                next_row = cls.edge_list[(nearest_turning + 1) % len(cls.edge_list)][0] # 周期循环长度
                # 无需考虑先后顺序, 因为farthest_turning == nearest_turning
                if (previous_row - row) * (row - next_row) > 0: # / or \ 走势, 改变一次
                    cnt = img_label[row, farthest_edge - 1]
                    assert cnt in (0,1) # 不可能是边界
                    return (cnt + 1) % 2
                elif (previous_row - row) * (row - next_row) < 0: # V 走势, 改变两次
                    cnt = img_label[row, farthest_edge - 1]
                    assert cnt in (0,1) # 不可能是边界
                    return (cnt + 2) % 2
                else:
                    print('不可能有平行线出现.')
                    raise ValueError
            elif nearest_turning_col < nearest_edge: # nearest_turning 与 nearest_edge 断开.
                cnt = img_label[row, farthest_edge - 1] # / or \ 走势, 改变一次
                assert cnt in (0, 1)  # 不可能是边界
                return (cnt + 1) % 2
            else:
                print('nearest_turning_col 不可能大于 nearest_edge')
                raise ValueError
        elif nearest_edge > farthest_edge: # 交点是一条线
            try:
                assert cls.edge_list[nearest_turning][0] == cls.edge_list[farthest_turning][0] #
            # nearest_edge 与 farthest_edge 本来就在 cols 上遍历得到, 无需确认 row 相同.
            except AssertionError:
                print('确认 nearest_turning 与 farthest_turning')
                print(nearest_turning, farthest_turning, position, cols, cls.edge_list[
                    nearest_turning][0], cls.edge_list[farthest_turning][0] )
                raise AssertionError

            # nearest_turning | farthest_turning | previous_point | next_point
            #       24        |     23           |      22        |     25
            #       23        |     24           |      22        |     25

            # 如果是从右向左划, 那么farthest_turning 在 nearest_turning 的后面.
            # 因此寻找 previous_row 应该是nearest_turning 与 farthest_turning 中col小的那个,
            # 在edge_list中的前面一个.
            # 通过前后端点走势进行判断

            if farthest_turning > nearest_turning:
                tmp = farthest_turning
                farthest_turning = nearest_turning
                nearest_turning = tmp
                tmp = None
            previous_row = cls.edge_list[(farthest_turning - 1) % len(cls.edge_list)][0]
            next_row = cls.edge_list[(nearest_turning + 1) % len(cls.edge_list)][0]
            if (previous_row - row) * (row - next_row) > 0:  # / or \ 走势, 改变一次
                cnt = img_label[row, farthest_edge - 1]
                assert cnt in (0, 1)  # 不可能是边界
                return (cnt + 1) % 2
            elif (previous_row - row) * (row - next_row) < 0:  # V 走势, 改变两次
                cnt = img_label[row, farthest_edge - 1]
                assert cnt in (0, 1)  # 不可能是边界
                return (cnt + 2) % 2
            else:
                print('不可能有平行线出现.')
                print(nearest_edge, farthest_edge, position, cols)
                print(cls.edge_list[nearest_turning], cls.edge_list[farthest_turning])
                print(cls.edge_list[nearest_turning + 1], cls.edge_list[farthest_turning - 1])
                print(cls.edge_list[nearest_turning-3:farthest_turning+3])
                print(previous_row, row, next_row)
                raise ValueError
        else:
            print('不可能交点既不是点, 又不是线.')
            print(nearest_edge, farthest_edge, position, cols)
            raise ValueError