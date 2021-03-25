class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        SEQUENCE_NUM = 3

        visits = [(username[i], timestamp[i], website[i]) for i in range(len(username))]
        visits = sorted(visits, key=lambda x: (x[0], x[1]))
        username_count = {}
        for name in username:
            if name in username_count:
                username_count[name] += 1
            else:
                username_count[name] = 1

        res = []
        cur_username = ""
        cur_user_3seqs = None
        cur_user_count = 0
        cur_site_visited = None
        for visit in visits:
            name, site = visit[0], visit[2]
            if username_count[name] < SEQUENCE_NUM:
                continue

            if name != cur_username:
                cur_username = name
                if cur_user_3seqs is not None and len(cur_user_3seqs) > 0:
                    res.append(cur_user_3seqs)
                cur_user_3seqs = []
                cur_user_count = 0
                cur_site_visited = set()
            else:
                cur_user_count += 1
            
            count_left = username_count[name] - cur_user_count - 1
            cur_user_3seqs = self.append_seq_list_per_user(cur_user_3seqs, site, cur_site_visited, count_left, SEQUENCE_NUM)
            cur_site_visited.add(site)
        
        if cur_user_3seqs is not None and len(cur_user_3seqs) > 0:
            res.append(cur_user_3seqs)

        res_set = {}
        for seqs in res:
            cur_user_set = set()
            for seq in seqs:
                if len(seq) == 3:
                    key = self.hashcode(seq)
                    if key in cur_user_set:
                        continue
                    cur_user_set.add(key)
                    if key in res_set:
                        res_set[key][1] += 1
                    else:
                        res_set[key] = [seq, 1]

        seq_count_list = []
        for key in res_set:
            seq_count_list.append((res_set[key][0], res_set[key][1], key))
        
        seq_count_list = sorted(seq_count_list, key=lambda x: (-x[1], x[2]))

        # max_count = -1
        # res = []
        # for seq_count in seq_count_list:
        #     if max_count == -1:
        #         max_count = seq_count[1]
        #     else:
        #         if seq_count[1] < max_count:
        #             break
        #     res.append(seq_count[0])
        return seq_count_list[0][0]

    def hashcode(self, seq):
        return "-".join(seq)

    def append_seq_list_per_user(self, seqs, website, cur_site_visited, count_left, max_length):
        extend_seqs = []
        for seq in seqs:
            if len(seq) < max_length and len(seq) >= max_length - count_left - 1:
                if len(seq) + count_left >= max_length:
                    seq2 = [s for s in seq]
                    extend_seqs.append(seq2)
                seq.append(website)

        if count_left >= max_length - 1 and website not in cur_site_visited:
            extend_seqs.append([website])
        seqs.extend(extend_seqs)
        return seqs


