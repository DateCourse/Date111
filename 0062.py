from collections import defaultdict


def solution(genres, plays):
    # 각 장르마다의 총 재생 횟수를 저장할 딕셔너리 생성
    total_plays = defaultdict(int)
    # 각 장르마다 노래의 정보를 저장할 딕셔너리 생성
    songs = defaultdict(list)
    # 노래의 개수
    n = len(genres)

    # 각 장르마다 총 재생 횟수와 노래의 정보를 저장
    for i in range(n):
        total_plays[genres[i]] += plays[i]
        songs[genres[i]].append((i, plays[i]))

    # 장르의 총 재생 횟수를 내림차순으로 정렬
    sorted_total_plays = sorted(total_plays.items(), key=lambda x: x[1], reverse=True)

    # 베스트 앨범에 들어갈 노래의 고유 번호를 저장할 리스트
    best_album = []

    # 각 장르마다 노래를 2개씩 선택
    for genre, _ in sorted_total_plays:
        # 해당 장르에 속한 노래를 재생 횟수 내림차순으로 정렬
        songs[genre].sort(key=lambda x: (-x[1], x[0]))
        # 해당 장르에 속한 노래가 2개 이상인 경우
        if len(songs[genre]) >= 2:
            best_album.extend([idx for idx, _ in songs[genre][:2]])
        # 해당 장르에 속한 노래가 1개인 경우
        else:
            best_album.append(songs[genre][0][0])

    return best_album


print(solution(genres, plays))

